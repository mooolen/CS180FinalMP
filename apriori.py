def generateSingleItemSet(transfile):
	itemSet = set()

	for line in datfile:
		for item in line.split(' '):
			itemSet.add(frozenset([int(item)]))

	return itemSet

def getSetOfFrequentKItemSet(transfile, transCount, itemSet, minSupport):
	datfile.seek(0)
	candidates = defaultdict(int)
	freqitemset = set()

	for item in itemSet:
		for line in datfile:
			if not line.isspace() and item.issubset(set(map(int,line.split(' ')))):
				candidates[item] += 1

	for item, supcount in candidates.iteritems():
		if supcount/transCount >= minSupport:
			freqitemset.add(item)

	return freqitemset, supcount/transCount


def getTransactionCount(datfile):
	transCount = 0
	for line in datfile:
		if not line.isspace():
			transCount += 1
	return transCount

def getNextCandidateItemSets(candidates):
	'''joining + pruning
	......
	......
	......

	return nextcandidates
	return None pag wala
	'''

def generateStrongRules(setoffreqitemset):
	''' setoffreqitemset is a list of itemsets with their corresponding support
		e.g. [ [{A},2], [{B},3], [{C},5], [{A,B},9] ]
	'''


def apriori(filename, minSupport, minConfidence):
	datfile = open(filename, 'r')			
	transCount = getTransactionCount()	#count number of transactions
	setoffreqitemset = []

	'''C_1 -- 1-itemset candidates '''
	candidates = generateSingleItemSet(datfile)	# generate 1-itemset candidates -> C_1 
	setoffreqitemset.append(getSetOfFrequentKItemSet(datfile, transCount, candidates, minSupport)) # count support/freq of each item, delete all items that has sup<minsup -> L_1
	i = 0


	while not setoffreqitemset is None:	#continue until generated frequent set is null
		candidates = getNextCandidateItemSets(setoffreqitemset[i][0])	#generate next candidates by joining sets, then prune -> C_2
		setoffreqitemset.append(getSetOfFrequentKItemSet(datfile, transCount, candidates, minSupport)) # count support/freq of each item, delete all items that has sup<minsup -> L_k
		i += 1

	generateStrongRules(setoffreqitemset)
