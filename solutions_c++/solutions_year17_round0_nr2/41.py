#include <bits/stdc++.h>
using namespace std;

int TC;
string S;

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		cin >> S;
		int infraction = -1;
		for (int i = 0; i < (int)S.length() - 1; i++) {
			if (S[i] > S[i + 1]) {
				infraction = i;
				break;
			}
		}
		if (infraction == -1) {
			printf("Case #%d: %s\n", tc, S.c_str());
			continue;
		}
		int prev = 0;
		for (int i = 1; i <= infraction; i++) {
			if (S[i] - S[i - 1] >= 1) prev = i;
		}
		S[prev]--;
		for (int i = prev + 1; i < S.length(); i++) S[i] = '9';
		if (S[0] == '0') {
			string ns = "";
			for (int i = 1; i < S.length(); i++) ns += S[i];
			S = ns;
		}
		printf("Case #%d: %s\n", tc, S.c_str());
	}
}
