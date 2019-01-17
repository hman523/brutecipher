#Brutecipher: a program to test all rotations to decrypt a cipher
#Author: Hunter Barbella (hman523)
#Date: 1/17/19
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Text to decode")
    parser.add_argument('-t', dest='text', required=True)
    args = parser.parse_args()
    text = str(args.text)
    text = text.lower()
    printAll(text)


if __name__ == '__main__':
    main()



