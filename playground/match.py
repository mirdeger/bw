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

#Kör igång crawler
print("starting crawler")
crawler = subprocess.Popen(['python3',str(crawl_script)], stdout=subprocess.PIPE)

for line in iter(crawler.stdout.readline,b''):
  attack_node(line.decode('utf-8')) #Right now the attacks happen sequentially.


#starta attackskript. TODO förbättring: sqlmap är slött. Bra att köra olika threads här!


  # # TODO:
  # fix popen
  # listener or loop, when new json comes in, save to file and run attack_node() (in new thread?)
