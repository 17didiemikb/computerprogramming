def something1():
	adjective = raw_input("Adjective: ")
	adjective2 = raw_input("Adjective: ")
	typobird = raw_input("Type of bird: ")
	room = raw_input("A room in a house: ")
	pastverb = raw_input("Past tense verb: ")
	verb = raw_input("Verb: ")
	relativenam = raw_input("Name of a relative: ")
	noun = raw_input("Noun: ")
	liquid = raw_input("Liquid: ")
	verbing = raw_input("Verb ending in -ing: ")
	bodypart = raw_input("Part of the body (plural): ")
	pluralnoun = raw_input("Plural noun: ")
	verbing2 = raw_input("Verb ending in -ing: ")
	noun2 = raw_input("Noun: ")
		
	print ("It was a %s, cold November day. I woke up to the %s smell of %s roasting in the %s downstairs. \
I %s down the stairs to see if I could help %s the dinner. My mom said, \
'See if %s needs a fresh %s.' So I carried a tray of glasses full of %s \
into into the %s room. When I got there, I couldn't believe my %s! There were %s \
%s on the %s!" % (adjective, adjective2, typobird, room, pastverb, verb, relativenam, noun, \
	liquid, verbing, bodypart, pluralnoun, verbing2, noun2))

play_again = 'y'
while play_again == 'y':
	something1()
	print('Do you want to play again? y/n: ')
	play_again = raw_input()
	
	