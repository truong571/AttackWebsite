with open('top50.txt','r' ,encoding='UTF-8') as fin:
    l_strip=[s.strip() for s in fin.readlines()]
fin.close()
lst=[]
for i in l_strip:
    lst.append(i)
    for j in range(10):
        lst.append(i+str(j))
result = open('listPass.txt','w')
for i in lst:
    result.write(i+'\n')