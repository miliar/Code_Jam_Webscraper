#include <sstream>
#include <iostream>
#include <string>

using namespace std;

int solve(char s[], int size, int casee) {
	//cout << "Solve case: " << s << " With size " << size << endl;
	
	int i = 0;
	int counter = 0;
	bool flipped[3100];
	int lastFlip;

	for (int i = 0; i < 3100; i++)
		flipped[i] = false;

	while (s[i] != 0) {
		if (flipped[i] && s[i] == '-') {
			//Ok we doen niets.
		} else if (!flipped[i] && s[i] == '+') {
			//Ok alles is oke
		} else {
			//cout << "Flip @ " << i << endl;

			lastFlip = i;
			for (int j = i; j < (i + size); j++)
				flipped[j] = !flipped[j];

			counter++;
		}

		i++;
	}

	if (lastFlip + size <= i) {
		cout << "Case #" << casee << ": " << counter << endl;
	}
	else {
		cout << "Case #" << casee << ": IMPOSSIBLE" << endl;
	}
};

int main() {
	int casee;
	int cases;

	cin>>cases;
	char s[3100];

	//cout << "Number of cases: " << cases << endl;
	
	for (casee = 1; casee <= cases; casee++ ) {
		int size;

		for (int i = 0; i < 3100; i++)
			s[i] = 0;
		cin >> s;
		cin >> size;
		solve(s, size, casee);
	}
};