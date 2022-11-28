   def init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):

      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
            elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

#
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

# Use the insert method to add nodes
root = Node(50)
root.insert(25)
root.insert(75)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(70)
root.insert(90)
root.insert(15)
root.insert(45)
root.insert(27)
root.insert(55)
root.insert(85)
root.insert(100)
