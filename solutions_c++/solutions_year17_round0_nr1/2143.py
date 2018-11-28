#include <iostream>
#include <map>
using namespace std;

string pancakes;
int flipper;
int flips;

map<char, char> reverse;

void flip(int start) {
	flips++;
	for (int i = start; i < start + flipper; i++)
		pancakes[i] = reverse[pancakes[i]];

}

bool possible() {
	for (int i = pancakes.length() - flipper; i < pancakes.length(); i++) {
		if (pancakes[i] == '-')
			return false;
	}
	return true;
}

int main() {
	reverse['-'] = '+';
	reverse['+'] = '-';
	int cases;
	cin >> cases;
	for (int case_counter = 1; case_counter <= cases; case_counter++) {
		cin >> pancakes;
		cin >> flipper;

		flips = 0;
		for (int i = 0; i <= pancakes.length() - flipper; i++)
			if (pancakes[i] == '-')
				flip(i);

		if (possible())
			cout << "Case #" << case_counter << ": " << flips << endl;
		else
			cout << "Case #" << case_counter << ": IMPOSSIBLE" << endl;

	}
	return 0;
}
