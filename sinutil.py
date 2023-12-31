import base64
import platform
import os
import subprocess
import datetime

print(".---------------.")
print("| _   _   _   _ |")
print("|| | | | (_) | ||")
print("|| |_| | | | | ||")
print("||  _  | | | |_||")
print("||_| |_| |_| (_)|")
print("'---------------'")

for i in range(3):
    print("                    ")

print("Welcome to sinutilities! Enter your command.")

while True:
    print("  ")
    command = input()
    
    if command == "mewo":
        print("mewo")
    elif command == "calc":
        print(eval(input("Enter your expression: ")))
    elif command == "base64enc":
        a = input("Enter what you want to encode with Base64: ")
        print(base64.b64encode(a.encode("UTF-8")).decode('UTF-8'))
    elif command == "base64dec":        
        a = base64.b64decode(input("Enter what you want to decode with Base64: "))
        print(a.decode('UTF-8'))
    elif command == "osfetch":
        if platform.system() == "Windows":
            ascii_windows = """
               55555
     45 555555555555
4444444 555555555555
4444444 444444444555
4444444 444444444444
                        You are using Windows!
4444444 444444444444
4444444 444444444444
4444444 444444444444
     44 444444444444
               44444
            """
            print(ascii_windows)
        elif platform.system() == "Linux":
            ascii_linux = """
        ###%        
       #.#.%%       
       #---*%       
       ----=%       
      #..:::%%%     
     #.....::%%%       You are using Linux!
     ........%%%#   
    -........%%%%   
  ----.......=%%=   
  ------....:=====  
    =---%%%%#===    
            """
            print(ascii_linux)
        elif platform.system() == "FreeBSD":
            ascii_freebsd = """
++#+   ++#++#   #++#
 +##+##+##++#++#++# 
 #+++#++##+##++#++  
 +##+#++#++##+##### 
 +##+##+#++#+++#++#+    You are using FreeBSD
 ++++#++##+##+#++#++
 ##+##++#++#+##+##+ 
  ++##+##++#++#++#+ 
   ++++##+##++#++   
      ++++##+#   
            """
            print(ascii_freebsd)
        elif platform.system() == "Darwin":  # MacOS has a system name of "Darwin"
            ascii_macos = """
           ##      
          ###       
    #############   
  ################  
 ################    
 ###############       You are using Mac Os!
 ################   
  ################ 
  ################  
     ##########       
            """
            print(ascii_macos)
        else:
            ascii_unknown = """
      ########      
    ############    
   ####      ####   
   ###       ####   
           #####    
         #####      What are you using? 
        ####        
        ###         
                    
        ####        
        ####        
            """
            print(ascii_unknown)
    elif command == "clear":
        os.system('clear' if os.name == 'posix' else 'cls')
    elif command == "date":
        print(datetime.datetime.now())
    elif command == "exit" or command == "quit":
        break
    elif command == "ping":
        host = input("Enter the host: ")
        try:
            # Using subprocess to ensure cross-platform compatibility
            result = subprocess.run(["ping", "-c 4", host], stdout=subprocess.PIPE, text=True)
            print(result.stdout)
        except Exception as e:
            print("Error:", str(e))
    elif command == "nslookup":
        domain = input("Enter the domain: ")
        try:
            result = subprocess.run(["nslookup", domain], stdout=subprocess.PIPE, text=True)
            print(result.stdout)
        except Exception as e:
            print("Error:", str(e))
    elif command == "help" or command == "?":
        print("""
mewo     - Just for fun.
calc     - Calculate mathematical expressions.
base64enc - Encode a string in Base64.
base64dec - Decode a Base64 string.
osfetch  - Display an ASCII representation of the current OS.
clear    - Clear the terminal screen.
date     - Display the current date and time.
ping     - Send ICMP echo requests.
nslookup - Lookup DNS information.
exit/quit - Terminate the program.
""")

    
    
    else:
        print("""
      ########      
    ############    
   ####      ####   
   ###       ####   
           #####    
         #####      I don't recognize that command. 
        ####        
        ###         
                    
        ####        
        ####        
        """)
