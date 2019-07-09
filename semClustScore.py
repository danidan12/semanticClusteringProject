#def getSemClustRank:

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

lists = np.unique(rec_evs.list)

#Semantic clustering on list-level
for l in range(len(lists)):
    #Get the list of recalled words in this list
    rec_words = 
    #Translate the recalled words in this list into wordvec vectors
    rec_vecs = 
    #Perform PCA    
    for k in range(11):
        pca = PCA(n_components = k)
        principalComponents = pca.fit_transform(rec_vecs)




#Semantic clustering on session-level