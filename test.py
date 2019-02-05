from itertools import islice

file_input = open("input.txt","r")
#x = f.readline().split(" ")
#print(x)
Line1 = list(map(int,file_input.readline().split(" ")))
#print(Line1)
#print(Line1[0]+3)
n,k = Line1[0],Line1[1]
#print(k)

Grades = []
for line in islice(file_input,0,n):
    Grades.append(int(line))
print(Grades)
