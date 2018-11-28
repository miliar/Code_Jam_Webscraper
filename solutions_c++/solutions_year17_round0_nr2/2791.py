#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
long long solve(int x) {
	long long res = 1;
	for (int i = 0; i < x; i++) {
		res *= 10;
	}
	return res;
}
string solve2(string S) {
	long long flag = 0;
	for (int i = 0; i + 1 < S.length(); i++) {
		if (S[i] > S[i + 1]) {
			for (int j = i + 1; j < S.length(); j++) {
				S[j] = '9';
			}
			flag = solve(S.length() - i - 1);
			break;
		}
	}
	return to_string(stoll(S) - flag);
}
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;
		string a = solve2(S);
		while (1) {
			string b = solve2(a);
			if (a == b) {
				break;
			}
			a = b;
		}
		printf("Case #%d: %s\n", t, a.c_str());
	}
}