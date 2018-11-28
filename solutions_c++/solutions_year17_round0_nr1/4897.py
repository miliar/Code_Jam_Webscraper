#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
using namespace std;

char flip(char side) {
	return side == '-' ? '+' : '-';
}

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	cin >> tt;

	for (int t = 1; t <= tt; t++) {
		string s;
		int k;
		cin >> s >> k;

		bool impossible = false;
		int step = 0;
		int size = s.size();
		for (int i = 0; i != size; i++) {
			if (s[i] == '-') {
				if (size - i >= k) {
					step++;
					for (int j = i; j != i + k; j++) {
						s[j] = flip(s[j]);
					}
				}
				else {
					impossible = true;
					break;
				}
			}
		}

		printf("Case #%d: ", t);
		if (impossible) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%d\n", step);
		}
	}

	fclose(stdout);
	return 0;
}