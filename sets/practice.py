info=[
("Alice","Math"),
("Bob","Science"),
("Charlie","Math"),
("Bob","Math"),
("Alice","English"),
("Charlie","English"),
]

s=set()
englishStudents=[]
records={}

for i in info:
  if records.get(i[0])==None:
    records.update({i[0]:set()})
    records[i[0]].add(i[1])
  else:
    records[i[0]].add(i[1])


  
for i in info:
  s.add(i[1])



uniqueSubject=[]
for j in s:
  uniqueSubject.append(j)

for k in info:
  if k[1]=="English":
    englishStudents.append(k[0])


print(uniqueSubject)
print(englishStudents)
print(records)


