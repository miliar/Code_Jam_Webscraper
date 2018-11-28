#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int maxt = 100;

_ULonglong find_tiny(_ULonglong in)
{
	_ULonglong res, diff=1;
	char str[20];
	int i,j;
	int findagain = 1;
	res = in;
	while (1) {
		memset(str, 0x00, sizeof(str));
		sprintf(str, "%llu", res);
		findagain = 0;
		for (i = strlen(str) - 1; i >0 ; i--) {
			diff = 1;
			//if (str[i] == '0') {
			//	for (j = strlen(str) - 1; j > i; j--)
			//		diff = diff * 10;
			//	res = res - diff;
			//	findagain = 1;
			//	break;
			//}

			if (str[i] < str[i - 1]) {
				str[i-1] = str[i-1]-1;
				for (int j = i; j < strlen(str); j++)
					str[j] = '9';
				char *pEnd;
				res = strtoull(str, &pEnd, 10);
				findagain = 1;
				//res--;
				break;
			}

		}
		//printf("%s ", str);
		if (findagain == 0)
			break;
	}
	return res;
}

void main() {
	int t, n;
	int loop = 0, b = 0;
	_ULonglong  bmk[101] = { 0 };
	_ULonglong work[101];
	int j;
	_ULonglong result =0;



	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> bmk[i];
		result = 0;
		if (bmk[i] < 10)
			result = bmk[i];
		else {
			
			result = find_tiny(bmk[i]);
		}
		
		cout << "Case #" << i << ": " << result << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}


// Usgae: MY_PROGRAM < input_file.txt > output_file.txt