import sys

arr =[]

filename = sys.argv[1]
with open(filename,'r') as rf:
	for line in rf.readlines():
		if line not in arr:
			arr.append(line)
with open('new_file.lst', 'w') as f:
	for i in arr:
		f.write(i)
