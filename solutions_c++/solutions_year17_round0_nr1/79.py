#include <bits/stdc++.h>

using namespace std;

void runTestCase(int t) {
	string s;
	cin >> s;
	int k;
	cin >> k;

	vector<bool> cakes(s.size(), false);

	for(int i = 0; i < s.size(); i++) {
		cakes[i] = s[i] == '+';
	}

	int ct = 0;
	for(int i = 0; i <= cakes.size() - k; i++) {
		if(!cakes[i]) {
			for(int j = 0; j < k; j++) {
				cakes[i+j] = !cakes[i+j];
			}
			ct++;
		}
	}

	for(int i = 0; i < cakes.size(); i++) {
		if(!cakes[i]) {
			ct = -1;
		}
	}

	cout << "Case #" << t << ": ";
	if(ct == -1) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << ct << endl;
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
