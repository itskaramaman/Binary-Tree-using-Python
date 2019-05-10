class Node:
	# initialize a node with its properties
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None


class BinaryTree(object):
	#initialize binary tree with its properties
	def __init__(self,root):
		self.root=Node(root)

	def preTraversal(self,start,traversal):
		# root => left =>right
		if start:
			traversal+=start.value+"-"
			traversal=self.preTraversal(start.left,traversal)
			traversal=self.preTraversal(start.right,traversal)
		return traversal	

	def inTraversal(self,start,traversal):
		# left => root => right
		if start:
			traversal = self.inTraversal(start.left,traversal)
			traversal+= start.value+"-"
			traversal= self.inTraversal(start.right,traversal)
		return traversal

	def postTraversal(self,start,traversal):
		# left => right => root
		if start:
			traversal= self.postTraversal(start.left,traversal)
			traversal=self.postTraversal(start.right,traversal)
			traversal+=start.value+"-"	
		return traversal	 


#  Making a graph
tree = BinaryTree('A')
tree.root.left=Node('B')
tree.root.right=Node('C')
tree.root.right.left=Node('X')
tree.root.right.right=Node('Z')
tree.root.left.left=Node('D')


print(tree.preTraversal(tree.root,""))
print(tree.inTraversal(tree.root,""))
print(tree.postTraversal(tree.root,""))

#          	 A
#		/ \
#              B   C
#	      /	   /\
#	     D    X  Z
#
#
