import os

a = open('./blog_edges.csv','r+b')
#with open('./blog_edges.csv','r+') as a:
net = a.read()
temp = net.replace(',',' ')
a.close()
b = open('./blog.edgelist','w')
b.write(temp)
#print(b)
b.close()