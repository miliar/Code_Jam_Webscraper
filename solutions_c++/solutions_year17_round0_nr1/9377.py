#include<iostream>

using namespace std;

char pancake[2001];
int false_idx = -1;
int flipper_width = 0;

int find_first_minux_index(int start) {
	int find = -1;
	for (int j = start; j < strlen(pancake); j++) {
		if (pancake[j] == '-') {
			find = j;
			break;
		}
	}

	return find;
}

int find_minimum() {

	bool find_first_minux_idx = false;
	int min = 0;
	while (false_idx !=-1) {

		if (strlen(pancake) - false_idx < flipper_width) return -1;

		min++;
		find_first_minux_idx = false;
		int i = false_idx;
		int limit = false_idx + flipper_width;
		for (i = false_idx; i < limit; i++) {
			if (pancake[i] == '-') {
				pancake[i] = '+';
			}
			else {
				pancake[i] = '-';
				if (find_first_minux_idx == false) {
					find_first_minux_idx = true;
					false_idx = i;
				}
			}
		}
		if (!find_first_minux_idx) {
			false_idx = find_first_minux_index(i);
		}
		
	}
	return min;
}


int main() {

	int cases = 0;
	cin >> cases;
	false_idx = 0;

	
	for (int i = 0; i < cases; i++) {
		cin >> pancake;
		cin >> flipper_width;

		false_idx = find_first_minux_index(0);
		for (int j = 0; j < strlen(pancake); j++) {
			if (pancake[j] == '-') {
				false_idx = j;
				break;
			}
		}

		if (false_idx == -1) {
			cout << "Case #" << i + 1 << ": 0" << endl;
		}
		else {
			int min = find_minimum();
			if (min == -1) {
				cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
			}
			else {
				cout << "Case #" << i + 1 << ": " << min << endl;
			}
		}
	}

}