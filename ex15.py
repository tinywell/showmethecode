from sys import argv

script,name = argv

file = open("ex15_sample.txt")
print file.read()
file.close()

print "script:",script