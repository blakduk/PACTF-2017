# Hash Killer

### Challenge
> Qu’est que c’est?
> We were clearing out the old server and came across a really weird *[file](hashes.txt)*...

### Hint
> Did someone say MD5? And that last line seems different from the rest…

### Solution
Looking at the txt file, there seems to be several hashes along with a base64 encoded string.
To decrypt the hashes, I use *[Hashkiller](https://hashkiller.co.uk/md5-decrypter.aspx)* as the problem title suggests. Copy all hashes to Hashkiller and I get the message:

	oh you wish it were this easy ? 
	sorry to let you down but this rabbit hole goes deeper !
	the word 'AES' hash is the key now decrypt me START

The message tells us it used AES to encrypt message with the key is the MD5 hash of 'AES'.
The last line of the file seems to be the base-64 encoded ciphertext.
My *([Python script](solution.py))* results the flag is flag{w3_l0v3_3ncrypt10n}
