#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int digit[100];
int a[100];
bool found;

void Back_Tracking(int i) {
	int lower_bound = 0;
	if (i == 0) {
		lower_bound = 1;
	}
	for (int j = digit[i]; j >= lower_bound; --j) {
		if (i > 0) {
			if (j < a[i - 1]) {
				break;
			}
		}
		a[i] = j;
		if (j < digit[i]) {
			for (int v = i + 1; v < n; ++v) {
				a[v] = 9;
			}
			found = true;
			return;
		}
		if (i + 1 < n) {
			Back_Tracking(i + 1);
		} else {
			found = true;
		}
		if (found) {
			return;
		}
	}
}

int main(int argc, char **argv) {
	string line;
	getline(cin, line);
	int nTests = atoi(line.c_str());
	for (int test = 1; test <= nTests; ++test) {
		getline(cin, line);
		n = line.length();
		for (int i = 0; i < n; ++i) {
			digit[i] = (int)(line[i] - '0');
		}
		found = false;
		Back_Tracking(0);
		if (found) {
			cout << "Case #" << test << ": ";
			for (int i = 0; i < n; ++i) {
				cout << a[i];
			}
			cout << endl;
		} else {
			cout << "Case #" << test << ": ";
			for (int i = 0; i < n - 1; ++i) {
				cout << "9";
			}
			cout << endl;
		}
	}
	return 0;
}