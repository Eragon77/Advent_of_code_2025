import os

script_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir, "input.txt")

dial=[]
for i in range (100):
    dial.append(i)

f=open(file_path)
input=f.readline()
i=50
total=0

while input!="":
    if input[0]=="R":
        rot=int(input[1:])

        for j in range(rot):
            if(i==99):
                i=0
            else:
                i+=1
            if i==0:
                total+=1

    elif input[0]=="L":
        rot=int(input[1:])

        for j in range(rot):
            if i==0:
                i=99
            else:
                i-=1
            if i==0:
                total+=1

    input=f.readline()

print(total)






