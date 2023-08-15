import pytesseract
from PIL import Image


def read_file(file_name):
	data= ""
	with open(file_name) as f1:
		data = f1.read()
	return data

def isValid(file_name):
	search_strings = ["cat /etc/shadow | w","cat /etc/shadow | head",
    "cat /etc/shadow | tail","date","2023"]
	content = read_file(file_name)
	
	search_results = {}
	for i in search_strings:
		if i in content:
			search_results[i] = True
		else:
			search_results[i] = False
	
	for i in search_results.keys():
		if search_results[i] == False:
			return False
			
	return True
	
	
# Execution starts here
print(isValid('output.txt'))

