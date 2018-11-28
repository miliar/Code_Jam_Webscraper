#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXN = 1002;
char pancake[MAXN];
int flipper;

int getResult() {
	int len = strlen(pancake);
	int result = 0;

	for (int i = 0; i + flipper <= len; i++) {
		if (pancake[i] == '-') {
			result++;
			for (int j = i; j < i + flipper; j++) {
				if (pancake[j] == '-') {
					pancake[j] = '+';
				}
				else {
					pancake[j] = '-';
				}
			}
		}
	}

	for (int i = len - flipper + 1; i < len; i++) {
		if (pancake[i] == '-') {
			return -1;
		}
	}

	return result;
}

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("a_small.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("a_large.out", "w", stdout);

	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {
		cin >> pancake >> flipper;
		
		cout << "Case #" << cnt << ": ";
		int result = getResult();
		if (result < 0) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << result << endl;
		}
	}

	return 0;
}