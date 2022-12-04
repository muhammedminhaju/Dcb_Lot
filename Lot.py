import random
group=[]
A=['Muhammed Minhaju a','Sreejith G','Sreelekshmi I.G','Christy George',\
   'Ashlin P.M','Gopika Rani', 'E Abhinaya','Sarathkumar R','Parvathy Jayarj',\
   'Mohammed Hakkim N','Bibin R','Akhila S','Mithun krishna','Amritha Raju',\
   'Arjun V.m','Alan Syed Muhammed S','Ashna T A','Preetha P','Aswany ks','Deepthi V M']

one_month_lott={"Course coordinator":"","Assistant semester coordinator":"",\
                "Introduction to Life Sciences & Bioinformatics":"","Applied Mathematics":"",\
                "Python Programming":"","Bioinformatics Lab I":"","Web programming and Databases (E)":""}
listkeys=one_month_lott.keys()
for i in listkeys:
  a=random.choice(A)
  A.remove(a)
  one_month_lott.update({i:a})
line="-"*70
print("||{}||".format(line.center(70)))  
for i in one_month_lott.keys():

  print("||{}||".format(" ".center(70)))
  i1=i
  i1.center(46)
  result=i1+':'+one_month_lott[i]
  print('||{}||'.format(result.center(70)))
  print("||{}||".format(" ".center(70)))
  print("||{}||".format(line.center(70)))