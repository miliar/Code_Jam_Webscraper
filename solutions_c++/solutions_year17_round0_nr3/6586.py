#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int maxt = 100;


int get_count(char *str, int sz) {
	// printf("processing: %s %d", str, sz);
	int i, res=0;
	int pcount = 0, mcount = 0;
	for (i = 0; i < strlen(str); i++) {
		if (str[i] == '+')
			pcount++;
		if (str[i] == '-')
			mcount++;
	}

	res = (int) mcount / sz;
	int bal = mcount % sz;
	//printf("processing: %s %d p=%d m=%d res=% bal=%d", str, sz, pcount, mcount, res, bal);
	if (bal == 0)
		return res;
	else if (bal == 1)
		return (-1);
	else if (pcount + mcount <= sz)
		return (-1);
	else if (bal % 2 == 0) {
		if (res >= 2)
			return (res + 1);
		else
			return (res + 2);
	}
	else  if ((sz - bal) % 2 == 0) {
		if (res >= 2)
			return (res + 2);
		else
			return (res + 3);
	}
	else
		return (-1);
}

void main() {
	int t,  sz, n, k, m;
	int min, max;
	int loop = 0, b = 0;
	char  bmk[101][1000] ;
	_ULonglong work[101];
	int j;
	_ULonglong result =0;
	char s[1003];
	int pos, diff;
	int newpos, newdiff;

	memset(bmk, sizeof(bmk), 0x00);
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		memset(s, 0x00, sizeof(s));
		cin >> n >> k;
		min = 0; max = 0;
		memset(s, '_', n+2);
		s[0] = 'o';
		s[n + 1] = 'o';
		s[n + 2] = 0x00;
		pos = 0;
		diff = n + 1;
		if (n==k) {
			max = 0; min = 0;
		}
		else {
			//cout << "01234567890" << endl;
			for (j = 0; j < k - 1; j++) {
				s[pos + (diff + 1) / 2] = 'o';
				//cout << s ;
				// find new position and max diff 
				newpos = 0;
				diff = 0;
				for (m = 0; m < n + 2; m++) {
					if (s[m] == 'o') {
						if (m - newpos > diff) {
							pos = newpos;
							diff = m - newpos;
						}
						newpos = m;
					}


				}
				//cout << diff << endl;

			}

			max = int((diff - 1) / 2);
			min = diff - 1 - 1 - max;
		}
		cout << "Case #" << i << ": " << max << " " << min << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}


// Usgae: MY_PROGRAM < input_file.txt > output_file.txt