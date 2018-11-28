#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("B-large.in","r",stdin);
	freopen("ou.txt","w",stdout);

	int t;
	cin >> t;
	for (int T = 1; T <= t; T++) {
		string s;
		cin >> s;
		int idx = 0;
		bool flag = false;
		for (int i = 0; i < s.size() - 1; i++) {
			if (s[i] > s[i + 1]) {
				flag = true;
				int j = i;
				while (j > 0 && (s[j] == 0 || s[j - 1] > s[j] - 1)) {
					j--;
				}
				if (j == 0)
					idx = (s[0] > '1') ? 0 : -1;
				else
					idx = j;
				break;
			}
		}
		cout << "Case #" << T << ": ";
		if (!flag)
			cout << s << endl;
		else {
			if (idx == -1) {
				for (int i = 0; i < s.size() - 1; i++)
					printf("9");
				printf("\n");
			} else {
				cout << s.substr(0, idx) << char(s[idx] - 1);
				for (int i = idx + 1; i < s.size(); i++)
					printf("9");
				printf("\n");
			}
		}
	}
}
