from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import sys
from termcolor import colored
html2term = {'lime':'green', 'maroon':'red', 'fuchsia':'red','aqua':'blue'}
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.currentcolor = "white"
	HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
	if (tag=="font"):
	    for attr in attrs:
		if (attr[0] == 'color'):
		    self.currentcolor = attr[1].lower()
		    if (html2term.has_key(self.currentcolor)):
			self.currentcolor = html2term[self.currentcolor]
    def handle_data(self, data):
	if (data!='\r\n'):
            print colored(data.replace('\r\n',''),self.currentcolor)
parser = MyHTMLParser()
for line in sys.stdin:
    parser.feed(line)