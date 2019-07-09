def getSemClustRank(wordsubset,wordfullset):

    import numpy as np

    nrecalls = len(wordsubset)
    ranks = np.zeros(nrecalls-1)

    for i in range(nrecalls-1):
        allDists = np.zeros(nrecalls-i)
        semDist = dist(wordsubset[i],wordsubset[i+1])



    return ranks