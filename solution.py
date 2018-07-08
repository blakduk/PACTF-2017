import md5
import base64
from Crypto.Cipher import AES

key = md5.new("AES").hexdigest()
cipher = base64.b64decode("mJRKaaMSR1atUGs0kOkAJP3dty9tjCvXKMzWDHtZdRQ=").encode("hex")
mess = AES.new(key, AES.MODE_ECB).decrypt(cipher)
print mess
