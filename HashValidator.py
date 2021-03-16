#!/usr/bin/env python

import sys
import os.path
from os import path
import hashlib
import tkinter as tk
from tkinter import filedialog

hashes = list(hashlib.algorithms_guaranteed)
bock_size = 65536 # The size of each read from the file
root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()



def menu():
	num = 0
	print("\n-----------Initial Menu-----------")
	for i in hashes:
		print(str(num) + ") " + i.upper())
		num +=1

	

def main():
	if path.exists(filename):
		menu()
		choice = int(input("Please type your choice (number): "))
		inputhash = str(input("Please type the hash you want to check: "))
		if choice < 0 or choice > len(hashes):
			print("\nInvalid input!!!")
			sys.exit()

		checksum = hashlib.new(hashes[choice])
		with open(filename, 'rb') as f:
			hashUpdate = f.read(bock_size)
			while len(hashUpdate) > 0:
				checksum.update(hashUpdate)
				hashUpdate = f.read(bock_size)

		print(checksum.hexdigest())
		print(inputhash)
		if checksum.hexdigest().lower().strip() == inputhash.lower().strip():
			print("\n[+] The hashes match. The file is intact!!!")
		else:
			print("\n[-] The hashes do not match. The file has been tampered!!!")
	else:
		print("[-] " + str(filename) + "path not found")
		sys.exit()


if __name__ == '__main__':
	main()
