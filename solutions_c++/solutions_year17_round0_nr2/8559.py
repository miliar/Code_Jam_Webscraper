#include <bits/stdc++.h>
using namespace std;

bool test(string s) {
	for (int i = 1; i < s.size(); i++)
		if (s[i] < s[i - 1])
			return false;
	return true;
}
int T;
string N;
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	scanf("%d", &T);
	cin.ignore();
	for (int t = 1; t <= T; t++) {
		getline(cin, N);
		for (int i = stoi(N); i > 0; i--) {
			if (test(to_string(i))==true) {
				cout << "Case #" << t << ": " << i << endl;
				break;
			}
		}
	}
	return 0;
}