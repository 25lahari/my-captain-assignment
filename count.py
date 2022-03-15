count={'i':0,'s':0,'p':0,'m':0}
word="mississippi"
def most_frequent(word):
        for i in word:
            if i=='m':
                    count['m']=count['m']+1

            elif i=='i':
                    count['i']=count['i']+1
            
            elif i=='s':
                    count['s']=count['s']+1

            else:
                    count['p']=count['p']+1
                    

        print("i=",count['i'],"s=",count['s'],"p=",count['p'],"m=",count['m'])

most_frequent(word)


