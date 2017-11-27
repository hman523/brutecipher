#Brutecipher: a program to test all rotations to decrypt a cipher
#Author: Hunter Barbella (hman523)
#Date: 11/27/17


def rot(code, num):
	newString = ""
	for i in range(0, len(code)):
		if code[i] is " ":
			newLetter = " "
		else:
			newLetter = "" + chr((ord(code[i])-97 + num)%26 + 97)
		newString = newString + newLetter
	return newString
		
def printAll(code):
	for x in range(0, 26):
		print(str(rot(code, x)) + ": Rot " +str(x))

text = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
text = text.lower()
printAll(text)


