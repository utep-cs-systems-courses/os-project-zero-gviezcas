import sys
import os

if len(sys.argv) is not 3:
    print("Correct Usage: wordCount.py <Input file name> <Output file name>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

if not os.path.exists("wordCount.py"):
    print("wordCount.py doesn't exist: Exiting")
    exit()

if not os.path.exists(inputFname):
    print("Input text file %s does not exist! Exiting" % inputFname)
    exit()

file = open(inputFname, "r")
words = []
counts = dict()

for line in file:
    words = line.lower().replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('-', ' ').replace("'", ' ').replace('"', '').split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

with open(outputFname, "w") as output:
    for key, value in sorted(counts.items(), reverse=False):
        output.write(str(key)+' '+str(value)+"\n")
    
output.close()

i = open(outputFname, "r")
print(i.read())
