inputfile = open('A-small-attempt2.in', 'r');
lines = inputfile.readlines();

problems = [];
results = [];
string = '';

def checkwinning(game):
	tplc = game.find('T');

	if tplc > 0:
		if (4 > tplc > -1):
			
			if game[0:1] == 'T':
				if(game[1:2] == game[2:3] == game[3:4] and game[1:2] != '.' and game[2:3] != '.' and game[3:4] != '.'):
					 
					return game[1:2];

				if(game[4:5] == game[8:9] == game[12:13] and game[4:5] != '.' and game[8:9] != '.' and game[12:13] != '.'):
					 
					return game[4:5];

				if(game[5:6] == game[10:11] == game[15:16] and game[5:6] != '.' and game[10:11] != '.' and game[15:16] != '.'):
					 
					return game[5:6];

			if game[1:2] == 'T':
				if(game[5:6] == game[9:10] == game[13:14] and game[5:6] != '.' and game[9:10] != '.' and game[13:14] != '.'):
					 
					return game[5:6];
				
				if(game[0:1] == game[2:3] == game[3:4] and game[0:1] != '.' and game[2:3] != '.' and game[3:4] != '.'):
					 
					return game[0:1];

			if game[2:3] == 'T':
				if(game[6:7] == game[10:11] == game[14:15] and game[6:7] != '.' and game[10:11] != '.' and game[14:15] != '.'):
					 
					return game[6:7];
				if(game[0:1] == game[1:2] == game[3:4] and game[0:1] != '.' and game[1:2] != '.' and game[3:4] != '.'):
					 
					return game[0:1];

			if game[3:4] == 'T':
				if(game[7:8] == game[11:12] == game[15:16] and game[7:8] != '.' and game[11:12] != '.' and game[15:16] != '.'):
					 
					return game[7:8];

				if(game[6:7] == game[9:10] == game[12:13] and game[6:7] != '.' and game[9:10] != '.' and game[12:13] != '.'):
					 
					return game[6:7];

				if(game[0:1] == game[2:3] == game[1:2] and game[0:1] != '.' and game[2:3] != '.' and game[1:2] != '.'):
					 
					return game[0:1];
		
		if (8 > tplc > 3):
			if game[4:5] == 'T':
				if (game[5:6] == game[6:7] == game[7:8] and game[5:6] != '.' and game[6:7] != '.' and game[7:8] != '.'):
					 
					return game[5:6];

				if (game[0:1] == game[8:9] == game[12:13] and game[0:1] != '.' and game[8:9] != '.' and game[12:13] != '.'):
					 
					return game[0:1]

			if game[5:6] == 'T':
				if (game[4:5] == game[6:7] == game[7:8] and game[4:5] != '.' and game[6:7] != '.' and game[7:8] != '.'):
					 
					return game[4:5];

				if (game[0:1] == game[10:11] == game[15:16] and game[0:1] != '.' and game[10:11] != '.' and game[15:16] != '.'):
					 
					return game[0:1];

				if (game[1:2] == game[9:10] == game[13:14] and game[1:2] != '.' and game[9:10] != '.' and game[13:14] != '.'):
					 
					return game[1:2];
			
			if game[6:7] == 'T':
				if (game[5:6] == game[4:5] == game[7:8] and game[5:6] != '.' and game[4:5] != '.' and game[7:8] != '.'):
					 
					return game[5:6];
				if (game[3:4] == game[9:10] == game[12:13] and game[3:4] != '.' and game[9:10] != '.' and game[12:13] != '.'):
					 
					return game[3:4];
				if (game[2:3] == game[10:11] == game[14:15] and game[2:3] != '.' and game[10:11] != '.' and game[14:15] != '.'):
					 
					return game[2:3];

			if game[7:8] == 'T':
				if (game[5:6] == game[6:7] == game[4:5] and game[5:6] != '.' and game[6:7] != '.' and game[4:5] != '.'):
					 
					return game[5:6];
				if (game[3:4] == game[15:16] == game[11:12] and game[3:4] != '.' and game[15:16] != '.' and game[11:12] != '.'):
					 
					return game[3:4];


		if (12 > tplc > 7):
			if game[8:9] == 'T':
				if(game[0:1] == game[4:5] == game[12:13] and game[0:1] != '.' and game[4:5] != '.' and game[12:13] != '.'):
					 
					return game[0:1];

				if(game[9:10] == game[10:11] == game[11:12] and game[9:10] != '.' and game[10:11] != '.' and game[11:12] != '.'):
					 
					return game[9:10];

			if game[9:10] == 'T':
				if(game[8:9] == game[10:11] == game[11:12] and game[8:9] != '.' and game[10:11] != '.' and game[11:12] != '.'):
					 
					return game[8:9];

				if(game[1:2] == game[9:10] == game[13:14] and game[1:2] != '.' and game[9:10] != '.' and game[13:14] != '.'):
					 
					return game[1:2];

				if(game[3:4] == game[6:7] == game[12:13] and game[3:4] != '.' and game[6:7] != '.' and game[12:13] != '.'):
					 
					return game[3:4];

			if game[10:11] == 'T':
				if(game[8:9] == game[9:10] == game[11:12] and game[8:9] != '.' and game[9:10] != '.' and game[11:12] != '.'):
					 
					return game[8:9];

				if(game[0:1] == game[4:5] == game[15:16] and game[0:1] != '.' and game[4:5] != '.' and game[15:16] != '.'):
					 
					return game[0:1];

				if(game[2:3] == game[6:7] == game[14:15] and game[2:3] != '.' and game[6:7] != '.' and game[14:15] != '.'):
					 
					return game[2:3];


			if game[11:12] == 'T':
				if(game[3:4] == game[7:8] == game[15:16] and game[3:4] != '.' and game[7:8] != '.' and game[15:16] != '.'):
					 
					return game[3:4];

				if(game[8:9] == game[9:10] == game[10:11] and game[8:9] != '.' and game[9:10] != '.' and game[10:11] != '.'):
					 
					return game[8:9];

		if (16 > tplc > 11):
			if game[12:13] == 'T':
				if(game[0:1] == game[4:5] == game[8:9] and game[0:1] != '.' and game[4:5] != '.' and game[8:9] != '.'):
					 
					return game[0:1];

				if(game[3:4] == game[6:7] == game[9:10] and game[3:4] != '.' and game[6:7] != '.' and game[9:10] != '.'):
					 
					return game[3:4];

				if(game[13:14] == game[14:15] == game[15:16] and game[13:14] != '.' and game[14:15] != '.' and game[15:16] != '.'):
					 
					return game[13:14];

			if game[13:14] == 'T':
				if(game[12:13] == game[14:15] == game[15:16] and game[12:13] != '.' and game[14:15] != '.' and game[15:16] != '.'):
					 
					return game[12:13];

				if(game[1:2] == game[5:6] == game[9:10] and game[1:2] != '.' and game[5:6] != '.' and game[9:10] != '.'):
					 
					return game[1:2];

			if game[14:15] == 'T':
				if(game[12:13] == game[13:14] == game[15:16] and game[12:13] != '.' and game[13:14] != '.' and game[15:16] != '.'):
					 
					return game[12:13];

				if(game[2:3] == game[6:7] == game[10:11] and game[2:3] != '.' and game[6:7] != '.' and game[10:11] != '.'):
					 
					return game[2:3];

			if game[15:16] == 'T':
				if(game[12:13] == game[13:14] == game[14:15] and game[12:13] != '.' and game[13:14] != '.' and game[14:15] != '.'):
					 
					return game[12:13];

				if(game[0:1] == game[5:6] == game[10:11] and game[0:1] != '.' and game[5:6] != '.' and game[10:11] != '.'):
					 
					return game[0:1];

				if(game[3:4] == game[7:8] == game[11:12] and game[3:4] != '.' and game[7:8] != '.' and game[11:12] != '.'):
					 
					return game[3:4];

	if (game[0:1] == game[1:2] == game[2:3] == game[3:4] and game[0:1] !=  '.' and game[1:2] != '.' and game[2:3] != '.' and game[3:4] != '.'):

		return game[0:1];

	if (game[0:1] == game[4:5] == game[8:9] == game[12:13] and game[0:1] !=  '.' and game[4:5] != '.' and game[8:9] != '.' and game[12:13] != '.'):

		return game[0:1];

	if (game[0:1] == game[5:6] == game[10:11] == game[15:16] and game[0:1] !=  '.' and game[5:6] != '.' and game[10:11] != '.' and game[15:16] != '.'):

		return game[0:1];

	if (game[1:2] == game[5:6] == game[9:10] == game[13:14] and game[1:2] !=  '.' and game[5:6] != '.' and game[9:10] != '.' and game[13:14] != '.'):

		return game[1:2];

	if (game[2:3] == game[6:7] == game[10:11] == game[14:15] and game[2:3] !=  '.' and game[6:7] != '.' and game[10:11] != '.' and game[14:15] != '.'):

		return game[2:3];

	if (game[3:4] == game[7:8] == game[11:12] == game[15:16] and game[3:4] !=  '.' and game[7:8] != '.' and game[11:12] != '.' and game[15:16] != '.'):

		return game[3:4];

	if (game[3:4] == game[6:7] == game[9:10] == game[12:13] and game[3:4] !=  '.' and game[6:7] != '.' and game[9:10] != '.' and game[12:13] != '.'):
		return game[3:4];

	if (game[4:5] == game[5:6] == game[6:7] == game[7:8] and game[4:5] !=  '.' and game[5:6] != '.' and game[6:7] != '.' and game[7:8] != '.'):

		return game[4:5];

	if (game[8:9] == game[9:10] == game[10:11] == game[11:12] and game[8:9] !=  '.' and game[9:10] != '.' and game[10:11] != '.' and game[11:12] != '.'):

		return game[8:9];

	if (game[12:13] == game[13:14] == game[14:15] == game[15:16] and game[12:13] !=  '.' and game[13:14] != '.' and game[14:15] != '.' and game[15:16] != '.'):

		return game[12:13];

	return False

def dawnorflight(game):

	if game.find('.') > -1:
		return 'Incomplete';
	else:
		return 'Dawn';

for x in lines:

	if x != '10\n' or x == '\n':

		readys = x.split('\n');

		string += readys[0]

		if len(string) == 16:
			problems.append(string);
			string = '';

for us in xrange(0, len(problems)):
	result1 = checkwinning(problems[us]);

	if result1 == False:
		result2 = dawnorflight(problems[us]);

		if result2 == 'Incomplete':
			result3 = 'Case #' + str(us + 1) + ': ' + 'Game has not completed';
			results.append(result3);

		if result2 == 'Dawn':
			result3 = 'Case #' + str(us + 1) + ': ' + 'Draw';
			results.append(result3);

	else:
		result3 = 'Case #' + str(us + 1) + ': ' + result1 + ' won';
		results.append(result3);

resultfile = open('result.txt', "w");
resultfile.writelines(["%s\n" % item  for item in results]);
resultfile.close();	