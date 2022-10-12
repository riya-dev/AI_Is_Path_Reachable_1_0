# Name: Riya Dev
# Date: 9/19/20

# Each Vertex object will have attributes to store its own name and its list of its neighboring vertices.
# ALL GOOD
class Vertex:
   def __init__(vertex, name, edgelist = []):
      vertex.name = name
      vertex.edge_list = edgelist

# If the file exists, read all edges and build a graph. It returns a list of Vertexes.   
# ALL GOOD
def build_graph(filename):
   try:
      infile = open(filename)
   except FileNotFoundError:
      print("File does not exist")
      return []
      
   graph = []
   for line in infile.readlines():
      left, right = line.strip().split()
      
      if left not in [v.name for v in graph]:
         graph.append(Vertex(left))
      if right not in [v.name for v in graph]:
         graph.append(Vertex(right))
         
      # add right to left's edgelist
      leftv = [x for x in graph if x.name == left][0]
      rightv = [x for x in graph if x.name == right][0]
      leftv.edge_list = leftv.edge_list[:] + [rightv]
      
   return sorted(graph, key = lambda x:x.name)

# prints all vertices and adjacent lists of the given graph.
# ALL GOOD
def display_graph(graph):
   for v in graph:
      edgelist = []
      for edge in v.edge_list:
         edgelist.append(edge.name)
      print(v.name, edgelist)

# checks if two Vertexes are reachable or not.  
# ALL GOOD
def is_reachable(fromV, toV):
   frontier = [fromV]
   explored = [fromV]
   
   if fromV.name == toV.name:
      return True
   
   while len(frontier) > 0:
      v = frontier.pop(0)
      for x in v.edge_list:
         if x.name == toV.name:
            return True
         if x not in frontier and x not in explored:
            frontier.append(x)
            exlored.append(x)
   return False

# returns the length of the path from a Vertex to the other Vertex. 
# If the other Vertex is not reachable, return -1.  (Ex) Path cost of A to B to C is 2. 
# ALL GOOD
def path_cost(fromV, toV):
   frontier = [fromV]
   explored = [fromV]
   path = {fromV: [fromV]}
   
   if fromV.name == toV.name:
      return 0
      
   while len(frontier) > 0:
      v = frontier.pop()
      for x in v.edge_list:
         if x.name == toV.name:
            return len(path[v])
         
         if x not in path:
            path[x] += path[v]
         elif len([x] + path[v]) < len(path[x]):
            path[x] = path[v] + [x]
         
         if x not in frontier and x not in visited:
            frontier.append(x)
            explored.append(x)
   
   return -1
   
# display_graph(build_graph("input.txt"))
# Test cases
g = build_graph(input("filename: "))   # build a graph

# To check if you build the graph with object correctly
for v in g:
   print (v, v.edge_list)
   
display_graph(g)                      # display the graph (edge list)
fromV, toV = None, None
print ("If you want to stop checking, type -1 for vertex values")
fromV_val, toV_val = input("From vertex value: "), input("To vertex value: ")    # Get vertex values from user

while fromV_val != '-1':
   # Find from and to Vertexes at graph
   for v in g:                         
      if v.name == fromV_val: fromV = v     
      if v.name == toV_val: toV = v

   if fromV is None or toV is None:
      print ("One or more vertex value does not exist.")
   else:
      print ("From {} to {} is reachable?".format(fromV_val, toV_val), is_reachable(fromV, toV))
      print ("Path cost from {} to {} is".format(fromV_val, toV_val), path_cost(fromV, toV))

   # Reset to test another case
   fromV_val, toV_val = input("\nFrom vertex value: "), input("To vertex value: ")
   fromV, toV = None, None
