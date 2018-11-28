#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

string s;

void go () {
	string res;
	bool f = 0;
	int beg = 0;

	for (int i = 0; i < (int)s.size() - 1; i++) {

		if (f) {
			res += '9';
		} else if (s[i] > s[i + 1]) {
			res += s[i];
			f = 1;
			if (s[beg] == '1') {
				for (int j = 0; j < (int)s.size() - 1; j++)
					cout << '9';
				cout << endl;
				return;
			} else {
				res[beg]--;
				for (int j = beg + 1; j <= i; j++)
					res[j] = '9';
			}
		} else {
			res += s[i];
		}

		if (s[i] < s[i+1])
			beg = i + 1;
	}
	if (f) cout << res << 9 << endl;
	else		cout << s << endl;
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> s;
		cout << "Case #" << t << ": ";
		go ();
	}

	return 0;
}
