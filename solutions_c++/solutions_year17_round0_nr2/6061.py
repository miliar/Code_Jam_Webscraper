#include <bits/stdc++.h>
using namespace std;

string ans(string n) {
	for (int i = n.size()-1; i > 0; i--) {
		if (n[i-1] <= n[i] && n[i-1] != '0')
			continue;
		else if (n[i-1] != '0') {
			n[i-1]--;
			for (int j = i; j < n.size(); j++) n[j] = '9';
		}
		else if (n[i-1] == '0') {
			int j = i-1;
			while (n[j] == '0') {
			 	n[j] = '9';
			 	j--;
			}
			n[j]--;
			for (int j = i; j < n.size(); j++) n[j] = '9';
			return ans(to_string(stoll(n)));
		}
	}
	return n;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	int iter = 1;
	while (iter <= t) {
		string n;
		cin >> n;

		cout << "Case #" << iter << ": " << stoll(ans(n)) << "\n";
		iter++;
	}
}