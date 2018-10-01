from collections import Counter
def countWordsUnstructured(filename):
	words = Counter()
	punc = ',.!?*&%$#'
	with open(filename) as in_file:
		for line in in_file:
			words.update(x.rstrip(punc).lower() for x in line.split())
	print (words)

countWordsUnstructured("./Bush_1991.txt")