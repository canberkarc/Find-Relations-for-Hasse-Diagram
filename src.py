def main_func(input_filename, output_filename):
	file = open(input_filename, "r")
	lines = file.readlines() # Read all lines from file

	# Detect how many lines are there in file
	count = 0
	for line in lines: 
		count += 1
	file.close()


	file = open(input_filename, "r")
	line = file.readline()
	
	# Loop to read contents from file
	# Number of relations to relationNum
	# Sets to sett
	# Relations to relations
	# relasetNum is a counter for sets
	count2 = 1 
	relaSetNum = 1
	relationNum = 0
	sett = []
	relations = []
	while (count2 != count):

		count2 += 1
		# Check if a valid input is read, otherwise print error message and exit
		if((line != "\n") and (line != "") and line[0].isnumeric() ):
			relationNum = int(line) # Read number of relations in relationNum
		elif(line == ""):
			break
		else: # If something entered that not expected, print Error!.
			print("Error, something entered that not expected!\n")
			

		# Read line, parse it and put its contents(just required ones) into list sett 
		line = file.readline()
		count2 += 1
		l = line.strip(",")
		for i in range(0,len(l),2):
			sett.append(l[i])
		sett.append("-") # This is for seperating sets

		# Length of list sett
		lenSett = len(sett)

		# Read relations into list relations
		for i in range(0,relationNum):
			line = file.readline()
			l = line.strip(",")
			relations.append((l[0],l[2]))
			count2 += 1 # Increment count2 for loop
		relaSetNum += 1 # Increment number of sets
		relations.append("-") # This is for seperating relations
		line = file.readline()
	file.close()

	out_file = open("output.txt","w") # Open output.txt in write mode

	ii = 0
	jj = 0
	sets = []
	relationss = []
	for i in range(1,relaSetNum):	 
		while (sett[ii] != "-"): # Get sets respectively from list sett to list sets, list sets will be empty after each iteration
			sets.append(sett[ii])
			ii += 1

		while (relations[jj] != "-"): # Get relations respectively from list relations to list relationss, list relations will be empty after each iteration
			relationss.append(relations[jj])
			jj += 1

		# Write to file
		out_file.write("n\n")

		if(checkError(sets,relationss) == True): # Check for error
			convert_to_POSET(sets, relationss) 
			
			out_file.write("POSET: ")
			for kx in relationss: # Write POSET
				ss = "(" + str(kx[0]) + ", " + str(kx[1]) + ")"
				if(kx != relationss[len(relationss)-1]): # If kx is not last element of relationss list then print with comma, otherwise print without comma
					out_file.write(ss + ", ")
				else:
					out_file.write(ss)
			out_file.write("\n")
			
			create_Hasse(sets, relationss)

			for kx in relationss: # Write Hasse Diagram
				ss = str(kx[0]) + "," + str(kx[1]) + "\n"
				out_file.write(ss)
			
		else:
			# If there is any error then print error for this input and go to next input
			out_file.write('Error! Unmatch between sets and their relations')
			break
		

		# Reset sets list for next sets
		if(ii != (lenSett - 1)): 
			ii += 1
			sets = [] # Reset sets list for next set
		
		# Reset relationss list for next relations	
		jj += 1
		relationss = [] # Reset relationss list for next relations
	out_file.close()

# Check if there is any unmatch between sets and their relations
def checkError(sets,relationss):
	ind1 = 0
	ind2 = 0
	chVal = True

	# Check if there is any other element from set in relations
	for ind1 in range(len(relationss)): # Loop of length relations
		for ind2 in range(0,2): # To reach elements of relations
			count = 0
			for k in sets: # Loop through set elements
				if(relationss[ind1][ind2] != k): # If elements of relation are different from all elements in set
					count += 1					 # count will be equal to length of sets and function will return False
			if(count == len(sets)):				 # otherwise will return True
				chVal = False
	return chVal			

def makeReflexive(sets,relationss):
	# I search for (x,x) in relations where x is sets' elements respectively, if there is no (x,x) in relationss, add it to relationss
	
	for k in sets:
		if((k,k) not in relationss):
			relationss.append((k,k))


def makeAntisymmetric(relationss):

	# With nested loop in relations, I compare if there is any antisymmetry or not and ignore same x and y(for example (a,a))
	for (x,y) in relationss:
		for (a,b) in relationss:
			if ((x != y) and (x == b) and (y == a)): # If there is an example that breaks antisymmetry
				relationss.remove((y,x)) # Delete relation that breaks antisymmetry

			if((x != y) and ((x != b) or (y != a))):
				pass

def makeTransitive(relationss): 
	count = 0
	extra_rela = [] # New relations to relationss to make it transitive if it's not transitive
	
	# Check if all relations are reflexive, if count is equal to length of relations then all relations are reflexive.
	for i in relationss:
		if(i[0] == i[1]):
			count += 1

	if(count == len(relationss)):
		pass
	else:
		# If not, with nested loop, check if there is any transitive relation without checking relations that have same elements
		# for example (a,a). If there is no transitive relation then add required relation to relationss
		# to have Transitivity
		for (a,b) in relationss:
			for (c,d) in relationss:
				if ((b == c) and (a != b) and ((a,d) in relationss)):
					pass
				elif((b == c) and (a != b) and ((a,d) not in relationss)):
					relationss.append((a,d))


# Function to convert relation to POSET if it's not.
def convert_to_POSET(sets, relationss):
	makeReflexive(sets,relationss) #Reflexivity function
	makeAntisymmetric(relationss) #Antisymmetric function
	makeTransitive(relationss) #Transitive function

def removeReflexive(sets,relationss):
	# In first loop, I take one element of set, let's call it as x. 
	# Then I search for (x,x) in relations, if there is then remove it from relationss list
		
	for k in sets:
		for i in relationss:
			if((i[0] == i[1]) and (i[0] == k) and (i[1] == k)):
				relationss.remove((k,k))

def removeTransitive(relationss): 
	count = 0
	
	# Check if all relations are reflexive, if count is equal to length of relations then all relations are reflexive.
	for i in relationss:
		if(i[0] == i[1]):
			count += 1

	if(count == len(relationss)): # If all relations consist of reflexive relations, do nothing
		return True
	else:
		rela = [] # I add relations that will be deleted to this list and then delete
				  # them from relationss list

		# With nested loop, check if there is any transitive relation without checking relations that have same elements for example (a,a).
		# If there is transitive relation, remove it 
		# else pass

		for (a,b) in relationss:
			for (c,d) in relationss:
				if ((b == c) and (a != b) and ((a,d) in relationss)):
					rela.append((a,d))
				elif((b == c) and (a != b) and ((a,d) not in relationss)):
					pass

		if(len(rela) >= 1): # If there is any relation to be deleted then delete from relationss list
			for k in rela:
				if(k in relationss): # If relation to be deleted is not deleted then delete it
					relationss.remove(k)

# Function to obtain Hasse Diagram
def create_Hasse(sets, relationss):
	removeReflexive(sets, relationss)
	removeTransitive(relationss)

if __name__ == '__main__':
	main_func("input.txt","output.txt")