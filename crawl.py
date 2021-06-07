from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import json
import pprint
import argparse

from Classes import *

parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument("--wivet", help="Run a wivet challenge, use 0 to run all")
parser.add_argument("--debug", action='store_true',  help="Dont use path deconstruction")
parser.add_argument("--url", help="Custom URL to crawl")
# Argument below was added by MATCHER-gang
parser.add_argument("--matcher", action='store_true', help="Used when the crawler is called by ModuleMatcher")
args = parser.parse_args()

# Clean form_files/dynamic
root_dirname = os.path.dirname(__file__)
dynamic_path = os.path.join(root_dirname, 'form_files', 'dynamic')
for f in os.listdir(dynamic_path):
    os.remove(os.path.join(dynamic_path, f))

WebDriver.add_script = add_script


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-xss-auditor")

# launch Chrome
driver = webdriver.Chrome(options = chrome_options) # driver = webdriver.Chrome(chrome_options = chrome_options)



#driver.set_window_position(-1700,0)

# Read scripts and add script which will be executed when the page starts loading
driver.add_script( open("js/lib.js", "r").read() )
driver.add_script( open("js/property_obs.js", "r").read() )
driver.add_script( open("js/md5.js", "r").read() )
driver.add_script( open("js/addeventlistener_wrapper.js", "r").read() )
#driver.add_script( open("js/ajax_interceptor.js", "r").read() )
#driver.add_script( open("js/ajax_observer.js", "r").read() )
driver.add_script( open("js/timing_wrapper.js", "r").read() )
driver.add_script( open("js/window_wrapper.js", "r").read() )
# Benjamin
driver.add_script( open("js/forms.js", "r").read() )
driver.add_script( open("js/xss_xhr.js", "r").read() )
driver.add_script( open("js/remove_alerts.js", "r").read() )

if args.wivet:
    challenge = int(args.wivet)
    if challenge > 0:
        url = "http://localhost/wivet/pages/" + str(challenge) + ".php"
    else:
        url = "http://localhost/wivet/menu.php"

    Crawler(driver, url).start()
elif args.url:
    url = args.url
    # The second argument matcher was added by MATCHER-gang
    Crawler(driver, url).start(args.debug, args.matcher)
else:
    print("Please use --wivet or --url")
