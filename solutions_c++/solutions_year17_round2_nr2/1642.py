#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int red, redYellow, yellow, yellowBlue, blue, blueRed;

#define RED 'R'
#define RED_YELLOW 'O'
#define YELLOW 'Y'
#define YELLOW_BLUE 'G'
#define BLUE 'B'
#define BLUE_RED 'V'

char unicorns[1001];
int n;
char first;

void defineFirst() {
	if (red >= yellow && red >= blue && red > 0) {
		first = RED;
		red--;
	} else if (yellow >= red && yellow >= blue && yellow > 0) {
		first = YELLOW;
		yellow--;
	} else if (blue >= red && blue >= yellow && blue > 0) {
		first = BLUE;
		blue--;
	} else if (redYellow >= yellowBlue && redYellow >= blueRed) {
		first = RED_YELLOW;
		redYellow--;
	} else if (yellowBlue >= redYellow && yellowBlue >= blueRed) {
		first = YELLOW_BLUE;
		yellowBlue--;
	} else {
		first = BLUE_RED;
		blueRed--;
	}
	unicorns[0] = first;
}

int defineNext(int i) {
	char previous = unicorns[i-1];
	char current;
	
	switch (previous) {
		case RED:
			if (yellowBlue > 0) {
				current = YELLOW_BLUE;
			} else if (yellow > blue) {
				current = YELLOW;
			} else if (blue > yellow) {
				current = BLUE;
			} else if (blue > 0 && yellow > 0) {
				if (redYellow < blueRed) {
					current = BLUE;
				} else if (redYellow > blueRed) {
					current = YELLOW;
				} else if (first == BLUE) {
					current = BLUE;
				} else {
					current = YELLOW;
				}
			} else {
				return 0;
			}
			break;
		case YELLOW:
			if (blueRed > 0) {
				current = BLUE_RED;
			} else if (red > blue) {
				current = RED;
			} else if (blue > red) {
				current = BLUE;
			} else if (blue > 0 && red > 0) {
				if (redYellow < yellowBlue) {
					current = BLUE;
				} else if (redYellow > yellowBlue) {
					current = RED;
				} else if (first == BLUE) {
					current = BLUE;
				} else {
					current = RED;
				}
			} else {
				return 0;
			}
			break;
		case BLUE:
			if (redYellow > 0) {
				current = RED_YELLOW;
			} else if (red > yellow) {
				current = RED;
			} else if (yellow > red) {
				current = YELLOW;
			} else if (yellow > 0 && red > 0) {
				if (blueRed < yellowBlue) {
					current = YELLOW;
				} else if (blueRed > yellowBlue) {
					current = RED;
				} else if (first == YELLOW) {
					current = YELLOW;
				} else {
					current = RED;
				}
			} else {
				return 0;
			}
			break;
		case RED_YELLOW:
			if (blue > 0) {
				current = BLUE;
			} else  {
				return 0;
			}
			break;
		case YELLOW_BLUE:
			if (red > 0) {
				current = RED;
			} else {
				return 0;
			}
			break;
		case BLUE_RED:
			if (yellow > 0) {
				current = YELLOW;
			} else {
				return 0;
			}
			break;
	}
	unicorns[i] = current;
	switch (current) {
		case RED:
			red--;
			break;
		case YELLOW:
			yellow--;
			break;
		case BLUE:
			blue--;
			break;
		case RED_YELLOW:
			redYellow--;
			break;
		case YELLOW_BLUE:
			yellowBlue--;
			break;
		case BLUE_RED:
			blueRed--;
			break;
		
	}
	
	
	
	return 1;
}

int isCornerValid(int n) {
	char last = unicorns[n-1];
	switch (first) {
		case RED:
			if (last == RED || last == RED_YELLOW || last == BLUE_RED) return 0;
			break;
		case YELLOW:
			if (last == YELLOW || last == RED_YELLOW || last == YELLOW_BLUE) return 0;
			break;
		case BLUE:
			if (last == BLUE || last == BLUE_RED || last == YELLOW_BLUE) return 0;
			break;
		case RED_YELLOW:
			if (last != BLUE) return 0;
			break;
		case YELLOW_BLUE:
			if (last != RED) return 0;
			break;
		case BLUE_RED:
			if (last != YELLOW) return 0;
			break;
	}
	return 1;
}
void solve () {
	int n;
	cin >> n;
	cin >> red;
	cin >> redYellow;
	cin >> yellow;
	cin >> yellowBlue;
	cin >> blue;
	cin >> blueRed;
	int i;
	defineFirst();
	for (i = 1; i < n; i++) {
		if (!defineNext(i)) {
			break;
		}
	}
	unicorns[n] = '\0';
	if (n == i && isCornerValid(n)) {
		cout << unicorns << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
//        cout << "IMPOSSIBLE " << unicorns << " n:" << n << " i:" << i << endl;
	}
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; i++) {
    	cout << "case #" << i << ": ";
    	solve();
	}
	return 0; 
}

