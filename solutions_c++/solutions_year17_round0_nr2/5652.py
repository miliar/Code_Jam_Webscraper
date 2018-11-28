#include <bits/stdc++.h>
using namespace std;

string s;
int T;


int main() {
	ios::sync_with_stdio(false);
	//freopen("B-large.in", "r", stdin);
	//freopen("Out.txt", "w", stdout);
	scanf("%d", &T);
	cin.ignore();
	for (int t = 1; t <= T; t++) {
		getline(cin, s);
		int l = 0, r = 0;
		for (int i = 1; i < s.size(); i++) {
			if (s[i] > s[i - 1]) {
				l = i;
				continue;
			}
			else if (s[i] == s[i - 1]) {
				r = i;
			}
			else {
				s[l]--;
				for (int k = l + 1; k <s.size(); k++) {
					s[k] = '9';
				}
			}
		}
		if (s[0] == '0'){
			int j = 1;
			while (s[j] == '0') {
				s[j] = '9';
				j++;
			}
			s.erase(0, 1);
		}
		cout << "Case #" << t << ": " << s << endl;
	}
	return 0;
}
