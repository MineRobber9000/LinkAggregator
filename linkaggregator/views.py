class View:
	"""A view. Used for anything visible."""
	def __init__(self, list):
		self.list = list;

	def printOut(self):
		print("----")
		for item in self.list:
			print(str(item))
			print("----")
