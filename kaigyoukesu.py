f = open("/Users/fujidai/sinTED/en-ja-100000.txt",'r')
#f = open("/Users/fujidai/Desktop/SINTED/en-ja-100000.txt",'r')

data = f.readlines()
#print(len(data))
#print(data)
aq=[]
for i in range(len(data)):
    data[i] = data[i].rstrip('\n')
    #print(data[i])
    aq.append(data[i])
    #print(i+1)
#print(len(data))
#print(aq)
#print(len(aq))



sw=[]
for i in range(len(aq)):
    if aq[i]=="":
        #print(i)
        sw.append(i)
        #print(data2[i],"!")
        #del data2[i]
        #print(i)
        

def remove_lines_from_file(file_path, sw):
    with open(file_path, 'r') as file:
        l = file.readlines()
    lines=[]
    for i in range(len(l)):
        l[i] = l[i].rstrip('\n')
        #print(data[i])
        lines.append(l[i])
    #print(len(lines))
    
    for i in sorted(sw, reverse=True):
        lines.pop(i)
    #print(lines)
    #print(len(lines))
    for i in range(len(lines)):
        print(lines[i])
    #print(len(lines))

# 使用例
file_path = '/Users/fujidai/sinTED/pseudo-pseudo-english-sentence-100000.txt'  # 対象のファイルパス
"消したいやつのファイル"

remove_lines_from_file(file_path, sw)











#