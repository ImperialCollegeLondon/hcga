# -*- coding: utf-8 -*-
# This file is part of hcga.
#
# Copyright (C) 2019,
# Robert Peach (r.peach13@imperial.ac.uk),
# Alexis Arnaudon (alexis.arnaudon@epfl.ch),
# https://github.com/ImperialCollegeLondon/hcga.git
#
# hcga is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hcga is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hcga.  If not, see <http://www.gnu.org/licenses/>.

import networkx as nx
import numpy as np

from functools import lru_cache

from ..feature_class import FeatureClass, InterpretabilityScore

featureclass_name = "ShortestPaths"


class ShortestPaths(FeatureClass):
    """ Shortest paths class """

    modes = ["fast", "medium", "slow"]
    shortname = "SP"
    name = "shortest_paths"
    keywords = []
    normalize_features = True

    def compute_features(self):
        """
        Compute the shortest path measures of the network

        Notes
        -----
        
        References
        ----------


        """
        @lru_cache(maxsize=None)
        def eval_shortest_paths(graph):    
            return nx.shortest_path(graph)


         # the longest path for each node
        largest_shortest_path = lambda graph: [len(list( eval_shortest_paths(graph)[u].values())[-1]) for u in  eval_shortest_paths(graph)]       
        self.add_feature(
            "largest_shortest_path",
            largest_shortest_path,
            "For each node we compute the shortest paths to every other node. We then find the longest 'shortest path' for each node.",
            InterpretabilityScore(3),
            statistics="centrality",
        )

        # the mean shortest path for each node
        mean_shortest_path = lambda graph: [np.mean([len(k) for k in list(eval_shortest_paths(graph)[u].values())]) for u in  eval_shortest_paths(graph)]       
        self.add_feature(
            "mean_shortest_path",
            mean_shortest_path,
            "For each node we compute the shortest paths to every other node. We then find the mean of the 'shortest paths' for each node.",
            InterpretabilityScore(3),
            statistics="centrality",
        )