s={1,2,2,2,3,5}
s5={1,2,2,2,3,5}
print(len(s))
print(s)
#add element in set s
s.add(5)

#remove a value from set
s.remove(5)

#pop()- removs a random val
s.pop()

#union
s2={6,6,6,7,2,2,3,8}
s3=s5.union(s2)
print(s3)

#intersection
s4=s5.intersection(s2)
print(s4)

# creating empty set
empty_set=set();
print(s)