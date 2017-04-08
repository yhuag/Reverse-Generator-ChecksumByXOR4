import sys
import enchant

# Initialization
ASCII_lowBound = 65
ASCII_highBound = 123
Checksum_width = 4

# The English library to validate words
d = enchant.Dict("en_US")


def generateChecksumByWord(word):
	result = []
	for i in xrange(Checksum_width):
		result.append(ord(word[i]) ^ ord(word[i + Checksum_width]))
	return result

# To generate a sequence of possible combination of
# ASCII codes XORed tuple given a target ASCII code
def generateByInt(target):
	result = []
	for i in xrange(ASCII_lowBound, ASCII_highBound):
		for j in xrange(ASCII_lowBound, ASCII_highBound):
			# Check the XORed result
			if ((i ^ j) == target):
				result.append((chr(i),chr(j)))
	return result

# Generate word sequence given different combination
# of ASCII codes, and check whether the word sequence
# is an English word
target_word = "Attacked"
target_checksum = generateChecksumByWord(target_word)
progress_id = 0		# The checking progress
possible_arr = []	# The possible final result

# Iteration through all the combinations
for (i1,j1) in generateByInt(target_checksum[0]):
	for (i2,j2) in generateByInt(target_checksum[1]):
		for (i3,j3) in generateByInt(target_checksum[2]):
			for (i4,j4) in generateByInt(target_checksum[3]):

				# Create the word string
				temp_str = ''.join([i1, i2, i3, i4, j1, j2, j3, j4])
				# Increase the progress by 1 step
				progress_id += 1

				# Log the progress per 100K steps
				if (progress_id % 100000 == 0):
					print "Processing..." + str(progress_id) + ": "

				# Check if some partial words existed in the word string
				if (d.check(temp_str[:4]) and d.check(temp_str[4:])):
					print temp_str
					possible_arr.append("4:"+temp_str)
				if (d.check(temp_str[:5]) and d.check(temp_str[5:])):
					print temp_str
					possible_arr.append("5:"+temp_str)
				if (d.check(temp_str[:6]) and d.check(temp_str[6:])):
					print temp_str
					possible_arr.append("6:"+temp_str)
				if (d.check(temp_str[:7])):# and d.check(temp_str[6:])):
					print temp_str
					possible_arr.append("7:"+temp_str)

# Print out the final result
print "==================================================="
print possible_arr
