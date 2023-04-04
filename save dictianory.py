import io
        
def save():
 i=0
 thisdict = {}
 with open('sub-test.csv', encoding='utf-8') as f:
     for line in f:
            #break
            word=line.split(",")
            word[1]= str(word[1])
            word[1]=word[1].replace('\n','')
            thisdict[word[0]]=word[1]
 #print(thisdict)
 words = []
 with open('sub-no_punct.txt', encoding='utf-8') as f:
     for line in f:
        for word in line.split():
            if word in thisdict.keys():
               continue
            else:
               finglish = input("enter the finglish equivelant for"+word +":")
               thisdict[word] = finglish

 with io.open('sub-test.csv','+a',encoding='utf-8-sig') as f:
    for k in thisdict:
      s = u''.join(k)
      s = u','.join([s,thisdict[k]]) + u'\n'
      f.write(s)
