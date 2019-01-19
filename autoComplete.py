# your code goes here
class TrieNode:
	def __init__(self):
		self.child = {}
		self.last = False
		
def insert(root, word):
	for i in range(len(word)):
		if word[i] not in root.child:
			root.child[word[i]] = TrieNode()
		root = root.child[word[i]]
	root.last = True
	
def search(root, word):
	for i in range(len(word)):
		if word[i] not in root.child:
			return False
		root = root.child[word[i]]
	return root and root.last
	
def delete(root, word, idx):
	if word and word[idx] not in root.child:
		return False
	if len(word) == idx+1:
		del root.child[word[idx]]
		if not root.child:
			return True
		return False
	else:
		node = root
		if delete(node.child[word[idx]], word, idx+1):
			if node.child:
				del node.child[word[idx]]
			return not node.child
		return False
		
def getRecur(root, temp, words):
	if root.last:
		words.append(temp)
	for a,n in root.child.items():
		getRecur(n, temp+a, words)
		
def printAutoComplete(root, prefix):
	temp = ''
	for i in range(len(prefix)):
		if prefix[i] not in root.child:
			return []
		temp += prefix[i]
		root = root.child[prefix[i]]
	
	if root.last and not root.child:
		return [prefix]
	words = []
	getRecur(root, temp, words)
	return words
	
root = TrieNode()
insert(root, "Hello")
insert(root, "Heleo")
insert(root, "Heap")
print(search(root, "Hello"))
delete(root, "Heap",0)
print(search(root, "Heap"))
insert(root, "Heap")
print(printAutoComplete(root,"Heapa"))
