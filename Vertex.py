
#import sys
#infinity = sys.maxint-1
infinity = 999999999999999

class Vertex:
	def __init__(self, name):
		self.id = name
		self.adjacent = {}
		self.pi = None
		self.key = infinity

	def add_neighboor(self, neighboor, weight=0):
#		add element to dictionary with [key] and value
		self.adjacent[neighboor] = weight

	def adjacentList(self):
			return list(self.adjacent.keys())

	def getKey(self):
		return self.key

	def setKey(self, k):
		self.key = k
