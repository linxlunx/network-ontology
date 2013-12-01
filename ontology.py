#!/usr/bin/env python

import networkx
from matplotlib import pyplot
from itertools import combinations
import json

# init graph
graph = networkx.Graph()

data = open("data.json")

# load data and iterate it
for line in data:

	# load json data
	temp = json.loads(line.strip())

	# get mention
	men = temp['post_entities_user_mentions']

	# define list for user temp (not unique)
	users_temp = []

	# append user to user temp list
	users_temp.append(temp['post_from_user'])

	# add mentioned user to the list
	if men != "null":
		for mention in men.split(","):
			users_temp.append(mention)

	# make list unique
	users = set(users_temp)

	# combine!
	graph.add_edges_from(combinations(users, 2))

# draw graph
networkx.draw(graph, node_size=5, font_size=8, width=.2)

# show graph
pyplot.show()
