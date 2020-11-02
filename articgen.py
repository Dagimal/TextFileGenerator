number_of_lines = len(open("kelurahanFilter.txt").readlines())
loop = -1
while loop <= number_of_lines:
	#loop += 1
	file = open("kelurahanFilter.txt", "r")
	lines = file.readlines()
	generator = lines[loop]
	
	print(generator)
	#export
	#daerah = print(generator, file=f)
	#f = open(str(loop) + "-kelurahan_" + daerah + ".md", "a")
	#frontmatter
	#print(("---"), file=f)
