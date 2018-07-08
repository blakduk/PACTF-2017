import itertools
import md5

val="1b657b7fe26eda5b3c1309d340f1674d"
charSet = "abc"
flag = 0
res = ""

#print md5.new("AHIIH").hexdigest()

for i in range (1,20):
    print "repeat = " + str(i)
    s = ([''.join(x) for x in itertools.product(charSet, repeat=i)])
    for h in s:
        if (md5.new(h).hexdigest() == val):
            res = h
            flag = 1
            break
    if (flag == 1):
        break
    
if res != "":
    print "Find a possible string: " + res
else:
    print "Nothing matches given hash"
        


