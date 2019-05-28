import RPi.GPIO as gp  # Import Raspberry Pi GPIO library
import urllib3
gp.setwarnings(False) # Ignore warning for now
gp.setmode(gp.Board) # Use physical pin numbering
gp.setup(18,gp.OUT) # Set pin 18 to be an output pin
true = 1
while(true): # RUN Forever
  try:
    http = urllib3.PoolManager()
    response = http.request('GET','http://automatesystem.epizy.com/project/buttonStatus.txt') #Open url link 
    status = response.data # Read data from url 
   
  except urllib3.exception.NewCoonectionError:
    print('Connection Failed')
  
 print(status)
 if status == " ON ":
    gp.output(18,True) #Turn ON
  
 if status == " OFF ":
    gp.output(18,False) #Turn OFF
