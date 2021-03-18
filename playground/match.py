#Mål: input match [kod med crawl()] [kod med attack()] URL
import sys
import os
import subprocess

def attack_node(json):
  print("starting attack in wrapper")
  attack = subprocess.run(['python3',str(attack_script), json], capture_output=True, text=True) #run ok because can wait until finish before comms.
  if attack.returncode==0:
    print(attack.args)
    print(attack.stdout)
  else:
    print("ERROR OCCURED IN ATTACKSCRIPT FOR NODE")
    print(attack.args)
    print(attack.stderr)


dir_path = os.path.dirname(os.path.realpath(__file__))
#TODO test whether these exist or something
crawl_script = dir_path+'/'+sys.argv[1]
attack_script = dir_path+'/'+sys.argv[2]
print("Wrapper running")
node_file = open("node_file.txt","a")
#Kör igång crawler
print("starting crawler")
crawler = subprocess.Popen(['python3',str(crawl_script)], stdout=subprocess.PIPE)

for line in iter(crawler.stdout.readline,b''):
  node_file.write(line.decode('utf-8')) # must be str
  attack_node(line.decode('utf-8')) #Right now the attacks happen sequentially
  #starta attackskript. TODO förbättring: sqlmap är slött. Bra att köra olika threads här!
node_file.close()



  # # TODO:
    # Check whether we can collect something else than stdout-> PIPE. Would be nice to print only intended data to match.py 
    #Attacks in separate threads so that the slow sqlmap scripts can be run concurrently.
