# networkx_adjacencymatrix
Implementing the adjacency matrix in a networkx un-directed graph.

Example of adjacency matrix using lists of lists:
Each node will have/not have weighted edges connected to another node. If looking directly horizontally, there are 0 edges meaning that the node won't have a feature for looping back to itself.

    W = [[0,2,1,3,9,4,_,_], # a 
        [_,0,4,_,3,_,_,_], # b 
        [_,_,0,8,_,_,_,_], # c 
        [_,_,_,0,7,_,_,_], # d 
        [_,_,_,_,0,5,_,_], # e 
        [_,_,2,_,_,0,2,2], # f 
        [_,_,_,_,_,1,0,6], # g 
        [_,_,_,_,_,9,8,0]] # h
