fin = open("Book1.txt")
fout = open("copy1.txt", "w+")
count = 0
page = 0 
pageno = int(input("enter a page number"))
for i in range(page)
    count=0:
    for i,val in enumerate(fin):
        s = val.strip("/n")
        for j in s:
            print(j)
            if j== 'O' or j== 'o':
                     h= '0'
                     fout.write(h)
            elif j== 'A' or j== 'a'
                     h= '4'
                     fout.write(h)
            elif j== 'E' or j== 'e'
                     h= '3'
                     fout.write(h)
            elif j== 'I' or j== 'i'
                     h= '1'
                     fout.write(h)
           else:
                     fout.write(j)


          fout.write('/n')
          print(s)
          count +=1
         if count==25:
             break
   page +=1

fout.close()

