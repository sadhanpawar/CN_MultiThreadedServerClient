import socket
import threading
import os.path

#UTA NAME : sadhan pawar vadegher
#UTA ID : 1002023295

# gives MIME type for each file format
def fetchcontenttype(filename):

    if ".htm" in filename or ".html" in filename:
        return "text/html"
    elif ".jpg" in filename or ".jpeg" in filename:
        return "image/jpeg"
    elif ".gif" in filename:
        return "image/gif"
    else:
        return "application/octet-stream"

def handleconnections(sock):

    statusline = ''
    poshttpresponsedata = "HTTP/1.0 200 OK\r\n"
    neghttpresponsedata = "HTTP/1.0 404 NOK\r\n"
    filefd = ''
    filedata = ''
    contenttype = 'Content-Type: '
    contentlenght = 'Content-Length: '
    connclose = 'Connection: close'
    finalhttpresponse = ''

    #receive the http request from socket. At max 4096 bytes can be received at once 
    data = sock.recv(4096)
    
    #tokenize the string to get the data for further processing.
    data = data.split()

    #display the http request message on console 
    
    if len(data) > 0 :

        print("--------------------------------------------------")
        print("--------------HTTP Request --------------------------")
        print(data)

        #handling only GET method in http request. Display error for any other request from clients
        if "GET" in data[0]:

            #extract filename from http request
            filename = data[1]
        
            #Check if the file exists. Process only if files is present
            if os.path.isfile(filename):
                #assign positive response for the status line
                statusline = poshttpresponsedata

                #fetch the content type as html/gif/jpeg
                contenttype = contenttype + fetchcontenttype(data[1]) + "\r\n"

                #read the contents of data to be sent to the client in body of the response
                with open(filename,'r') as filefd:
                    filedata = filefd.read()

                contentlenght = contentlenght + (str(len(filedata))) + "\r\n"
            else:

                #file doesn't exists. Assign negative response to the statusline
                statusline = neghttpresponsedata
                contenttype = contenttype + "text/html" + "\r\n"
                filedata = "<HTML>" \
                "<HEAD><TITLE>Not Found</TITLE></HEAD>" \
                "<BODY>Not Found</BODY></HTML>"
                contentlenght = contentlenght + (str(len(filedata))) + "\r\n"

        else:
            #only handling GET method in http request. Decline all the other methods if requested
            statusline = neghttpresponsedata
            contenttype = contenttype + "text/html" + "\r\n"
            filedata = "<HTML>" \
                        "<HEAD><TITLE>ONLY GET METHOD IS SUPPORTED !!! </TITLE></HEAD>" \
                        "<BODY>ONLY GET METHOD IS SUPPORTED !!! </BODY></HTML>"
            contentlenght = contentlenght + (str(len(filedata))) + "\r\n"

        #send the status, content type for MIME type and data
        finalhttpresponse = statusline + contenttype + contentlenght + "\r\n"
        sock.send(finalhttpresponse)
        sock.sendall(filedata)
    #close the socket after completing the session
    sock.close()
     
def invokeServer():

   host = "localhost"
   port = 8998 #port number configured

   #Create a socket with communication TCP connection two way connection based byte stream
   socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
   
   #Bind the hostname which is a loopback address and unknown port number range more than 1024
   socketfd.bind((host,port))

   #be in the listening mode to accept connections from clients
   socketfd.listen(1)

   print("Server started listening at ........",port)

   while True: 
       #when a connection is made accept call will accept it. the return is new connection socket and
       #the address bound to that socket
       newconnectionsocket, address = socketfd.accept()
       
       #print the new socket and address for reference purpose for debugging 
       #print(newconnectionsocket)
       #print(address)
       
       # multi threaded server which will be ready to accept new incoming connections simulatenously while processing
       # already existing socket connections
       threads = threading.Thread(target=handleconnections,args=(newconnectionsocket,))
       
       #start a thread with new socket connection passed 
       threads.start()

if __name__ == '__main__':
    invokeServer()
