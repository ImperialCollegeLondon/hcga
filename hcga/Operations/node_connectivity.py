# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:30:46 2019

@author: Rob
"""

import numpy as np
import networkx as nx

class NodeConnectivity():
    def __init__(self, G):
        self.G = G
        self.feature_names = []
        self.features = []

    def feature_extraction(self):

        """Compute node connectivity measures.

        Parameters
        ----------
        G : graph
           A networkx graph

        Returns
        -------
        feature_list :list
           List of features related to node connectivity.


        Notes
        -----
        Implementation of networkx code:
            https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/approximation/connectivity.html#all_pairs_node_connectivity

        
        References
        ----------
        .. [1] White, Douglas R., and Mark Newman. 2001 A Fast Algorithm for 
        Node-Independent Paths. Santa Fe Institute Working Paper #01-07-035
        http://eclectic.ss.uci.edu/~drwhite/working.pdf

        """

        self.feature_names = ['mean','std','median']

        G = self.G

        feature_list = []

        # calculating node connectivity
        node_connectivity = nx.all_pairs_node_connectivity(G)

        N = G.number_of_nodes()
        
        node_conn = np.zeros([N,N])
        for key1, value1 in node_connectivity.items():    
            for key2, value2 in value1.items():
                node_conn[key1,key2] = value2
    
        
        # mean and median minimum number of nodes to remove connectivity
        feature_list.append(node_conn.mean())
        feature_list.append(node_conn.std())
        feature_list.append(np.median(node_conn))

        # fitting the node connectivity
        
        
        

        self.features = feature_list