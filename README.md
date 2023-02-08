# CN_MultiThreadedServerClient

Language:   		python
compiler:   		python
modules:    		threading, socket, os
OS:         		Ubuntu/wsl 
IDE:        		command line terminal
Command/Compile:    	python server.py in wsl or ubuntu
Files needed:		image.jpg, index.html, giphy.gif
workspace:		/home/sadhan/computerNetworks/ (varies according to different workspace)

URLs Tested:
    - http://localhost:8998/home/sadhan/computerNetworks/index.html -> (file exists)positive response from server
    - http://localhost:8998/    -> negative response from server
    - http://localhost:8998/home/sadhan/computerNetworks/in.htm -> (file doesn't exists) negative response from server
    - http://localhost:8998/home/sadhan/computerNetworks/image.jpg -> (file exists) positive response from server
    - http://localhost:8998/home/sadhan/computerNetworks/giphy.gif -> (file exists) positive response from server 

   
Different workspace:
	
	Please use your own workspace
	workspace:	/home/sadhan/computerNetworks/ (varies according to different workspace)

	Example:
    		- http://localhost:8998/{workspace}/giphy.gif -> (file exists) positive response from server 
