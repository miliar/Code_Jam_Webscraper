#include <bits/stdc++.h>
using namespace std;

void flipString(string& s,int from, int to) {
	for (int i = from; i < to; i++)
		s[i] = (s[i] == '-'? '+' : '-');
}

bool isHappy(string& s, int k) {
	int start = 1 + (int)s.size() - k;
	int end = (int)s.size();
	for (int i = start; i < end; i++) {
		if (s[i] == '-')
			return false;
	}
	return true;
}

int main() {

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) { //test cases
		string s;
		int k;
		cin >> s >> k;

		int num_flips = 0, length = (int)s.size();
		for (int i = 0; i+k <= length; i++) {
			if (s[i] == '-') {
				num_flips++;
				flipString(s, i, i+k);
			}
		}

		cout << "Case #" << t << ": ";
		if(isHappy(s, k))
			cout << num_flips << '\n';
		else cout <<  "IMPOSSIBLE" << '\n';
	}

	return 0;
}
