class Post:
	"""A post. Used for a link."""
	def __init__(self,title,link,description,author):
		self.title = title;
		self.link = link;
		self.desc = description;
		self.author = author;
		self.score = 0;

	def __str__(self):
		return "Score: "+str(self.score)+"; "+self.title+" (submitted by "+self.author.name+")"

	def read(self):
		print("----")
		print("Score: "+str(self.score))
		print(self.title+" ("+self.link+")")
		print("Author: "+self.author.name+" ("+self.author.id+")")
		print("Description: "+self.desc)

class Author:
	"""An author."""
	def __init__(self, name, id):
		self.name = name;
		self.id = id;
