import os

script_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir, "input.txt")

f=open(file_path)
string=f.readline()

total=0

while len(string) > 0:
    found=string.find(",")
    
    if(found==-1):
        range_str=string
        string="" 
    else:
        range_str=string[:found]
        string=string[found+1:]

    r1=int(range_str[:range_str.find("-")])
    r2=int(range_str[range_str.find("-")+1:])

    for i in range(r1,r2+1):
        s=str(i)
        if len(s)%2!=0:
            continue

        #index starts at 0
        half=len(s)//2
        
        if s[:half]==s[half:]:
            total+=int(s)

print(total)