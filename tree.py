class Tree:
	class Node: # Класс в классе можно делать, т.к. в классе описано свое пространство имен
		def __init__(self, data):
			self.parent = None
			self.left = None
			self.right = None
			self.key = data
	def __init__(self):
		self.root = None

	def find(self, data): 
		p = self.root
		while p is not None and p.key != data: # Важна последовательность написаний условий, т.к. может быть ошибка при проверке ключа
			if data > p.key:
				p = p.right
			else:
				p = p.left
		return p

	def insert(self, data):
		p = self.find(data) # Одно и то же число не может храниться дважды, как в множестве, но значения могут повторяться if p is not None: return
		if p is not None:
			return
		node = Tree.Node(data)
		if self.root is None:
			self.root = node
			return
		p = self.root
		while True:
			if data < p.key:
				if p.left is None:
					p.left = node
					node.parent = p
					break
				else:
					p = p.left
			else:
				if p.right is None:
					p.right = node
					node.parent = p
					break
				else:
					p = p.right

	def print_tree(self, node):
		if node is None:
			return
		self.print_tree(node.left)
		print(node.key)
		self.print_tree(node.right)


T = Tree()
T.insert(5)
T.insert(7)
T.insert(2)
T.print_tree(T.root)