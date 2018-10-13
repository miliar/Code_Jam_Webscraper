f = open('A-small-attempt0.in', 'r');
o = open('output', 'w');

def friends(sentence, count):
	sentence = sentence.replace(" ", "");
	numbs = [c for c in sentence];
	numbs = [int(numeric_string) for numeric_string in numbs];
	max = numbs[0];
	numbs.pop(0);
	print numbs;

	people = 0;
	addative = 0;
	i = 0;
	while i < len(numbs):
		if i == 0:
			people = numbs[i];
		else:
			if people < i:
				addative += i-people;
				people += i-people;
			people += numbs[i];
		i += 1;
	o.write('Case #' + str(count) + ': ' + str(addative) + '\n');

case_number = 1
for x in f.readlines()[1:]:
  x = x[:len(x)-1];
  friends(x, case_number);
  case_number += 1;