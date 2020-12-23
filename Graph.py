
from Vertex import *

class Graph(): #el grafo en esencia es un diccionario
	def __init__(self):
		self.G = {}
		self.num_vertices = 0

	def add_vertex(self, name):
		new_vertex = Vertex(name)
		self.G[name]  = new_vertex
		self.num_vertices = self.num_vertices + 1

	def add_edge(self, start, end, weight = 0, diagraph = 0):
		if start not in self.G:
			self.add_vertex(start)
		if end not in self.G:
			self.add_vertex(end)
		if diagraph == 1:
			self.G[start].add_neighbor(self.G[end], weight)
		else:
			self.G[start].add_neighbor(self.G[end], weight)
			self.G[end].add_neighbor(self.G[start], weight)

	def get_vertices(self):
		return list(self.G.values())

	def set_startNode(self, start):
		self.G[start].key = 0
