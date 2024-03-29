from pprint import pprint, pformat

debug = True

def log(msg):
	if debug: print(msg)

def plog(msg):
	if debug: pprint(msg)

INDENT = "  "

def indent(s):
	return s.replace("\n", "\n" + INDENT)