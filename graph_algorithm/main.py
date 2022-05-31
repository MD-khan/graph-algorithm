#!/usr/bin/env python3

# get the value from a graph

def depth_first_value(graph, source):
    stack = [ source ] # a 

    while len(stack) > 0:
        current = stack.pop() # remove the stack value and set it current
        print(current, end=" ")
        for neighbor in graph[current]:
            stack.append(neighbor)

graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

depth_first_value(graph,'a') # abdfc

#print(graph)