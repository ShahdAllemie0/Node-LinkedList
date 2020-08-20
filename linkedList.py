class Node:
  def __init__(self,year,highlight,nnext=None):
    self.highlight=highlight
    self.year=year
    self.nnext=nnext

  def getData(self):
    dictt={"Year": self.year, "highlight": self.highlight}
    return dictt

  def get_year(self):
    return self.year
  def get_highlight(self):
    return self.highlight
  def get_next(self):
    return self.nnext
  def set_year(self, year):
    self.year=year
  def set_hilight(self, highlight):
    self.highlight=highlight
  def set_next(self, node):
    self.nnext=node #why node


class LinkedList:
  def __init__(self,year,highlight):
    self.head=Node(year,highlight)
    self.tail=self.head
   
  def getHead(self): 
    return self.head

  def insert(self,year,highlight): 
    newNode=Node(year,highlight) 
    newNode.set_next(self.head)
    self.head=newNode

  def getData(self): 
    data=[]
    currentNode=self.getHead()
    while currentNode:
      if currentNode.getData()!= None:
        data.append(currentNode.getData())
      currentNode=currentNode.get_next()
    return data  


  def get_node(self):
    current_node=self.getHead()
    while current_node:
      if current_node.get_year()!=None:
        print(f"{current_node.get_year()}-{current_node.get_highlight()}")
      current_node=current_node.get_next()
s=LinkedList(7, "I go to school")
s.insert(2,"I can eat all kinds of food")
s.insert(0, "I was born")

current_node=s.getHead()
count=0
for x in s.getData():
  print(f'Node {count}:{x}')
  count+=1
age = int(input("what is your age?"))-1

while current_node.get_year() <= age:
  current_age = current_node.get_year()+1
  if current_node.get_next() != None and      current_node.get_next().get_year()==current_age:
    current_node=current_node.get_next()
  else:
    highlight = input (f"what is your highlight for the {current_age} Year ?")
    new_node = Node(current_age, highlight, current_node.get_next())
    current_node.set_next(new_node)
    current_node = new_node
count=0
for x in s.getData():
  print(f'Node {count}:{x}')
  count+=1 


# ageee=int(input("Your age: "))
# s=LinkedList(7,"I turned seven")
# s.insert(3,"I started walking")
# s.insert(1,"I was born")


# k=1
# lenght=((len(s.getData())))
# agee=int(ageee)-lenght
# lis=[]
# lis2=[]
# m=1
# while m!=ageee+1:
#   lis.append(m)
#   m+=1

# for w in s.getData():
#   lis2.append(w["Year"])
  # if w["Year"] not in lis and w["Year"] not in lis2 :
  #   lis2.append(w["Year"]) 



# lis3=[]
# for l in lis: 
#      if l not in lis2:
#        lis3.append(l)
#        h=input(f'Please enter Highlight of {l}year ')
#        s.insert(l,h)
# c=1
# for g in s.getData():  
#    print(f'Node {c}:{g}') 
#    c=c+1       

# while 0!=(agee): 
  
#   for l in range(k,ageee):  
#     print(f)
#     for f in s.getData():
#       if l != f["Year"] and l not in lis:
#         lis.append(l)
       
#         h=input(f'Please enter Highlight of {l}year ')
#         s.insert(l,h)
  
#   # y=input(f'Please enter the year ')
#   # h=input(" Highlight: ")
#   # s.insert(int(y),h)
#   agee-=1

# print(lis)  
# print(lis2)
# print(lis3)
