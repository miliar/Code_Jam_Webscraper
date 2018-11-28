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
int k;

void go () {
	int res = 0;

	for (int i = s.size() - 1; i >= 0; i--) {
		if (s[i] == '-') {
			for (int j = i - k + 1; j <= i; j++) {
				if (j < 0) {
					cout << "IMPOSSIBLE" << endl;
					return;
				}
				if (s[j] == '+') s[j] = '-';
				else			 s[j] = '+';
			}
			res++;
		}
	}

	if (res == -1)	cout << "IMPOSSIBLE" << endl;
	else	cout << res << endl;
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> s >> k;
		go ();
	}

	return 0;
}
