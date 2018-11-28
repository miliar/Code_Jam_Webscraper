#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll go() {
	string S;
	cin >> S;
	string ans;

	for (int i = 0; i < S.size(); i++) {
		for (char j = '9'; j >= '0'; j--) {
			//is there anything?
			string t = ans;
			while (t.size() < S.size()) {
				t += j;
			}

			if (t > S) {
				continue;
			}

			ans += j;
			break;
		}
	}

	stringstream ssans(ans);
	ll ssansx;
	ssans >> ssansx;
	return ssansx;
}

int main() {
	freopen("bin.in", "r", stdin);
	freopen("bout.out", "w", stdout);
	int nq;
	cin >> nq;
	for (int i = 1; i <= nq; i++) {
		cout << "Case #" << i << ": " << go() << '\n';
	}
}
