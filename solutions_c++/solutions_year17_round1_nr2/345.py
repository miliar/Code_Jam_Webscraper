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

const int N = 55;
int n, p, r[N];
queue <int> q[N];

int val[N], mn[N], mx[N];

int go () {
	int res = 0;

	memset (val, 0, sizeof val);
	int sz = 1;
	bool f = 0;
	while (sz) {
		sz = INF;
		if (!f) {
			for (int i = 0; i < n; i++) {
				val[i] += r[i];
			}
		}

		for (int i = 0; i < n; i++) {
			mx[i] = (val[i] * 11)/10;
			mn[i] = (val[i] * 9 + 9)/10;
		}
/*
		for (int i = 0; i < n; i++)
			cout << val[i] << " ";	cout << endl;
		for (int i = 0; i < n; i++)
			cout << mn[i] << " ";	cout << endl;
		for (int i = 0; i < n; i++)
			cout << mx[i] << " ";	cout << endl;
*/

		f = 1;
		for (int i = 0; i < n; i++) {
			while (q[i].size() and q[i].front() < mn[i])
				q[i].pop();

			if (!q[i].size() or q[i].front() > mx[i])
				f = 0;

			sz = min ((int)q[i].size(), sz);
		}

		if (f) {
			for (int i = 0; i < n; i++) {
				q[i].pop();
				sz = min ((int)q[i].size(), sz);
			}
		}

/*		cout << f << endl;
		cout << endl;
*/
		res += f;
	}

	return res;
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> p;

		for (int i = 0; i < n; i++)
			cin >> r[i];

		for (int i = 0; i < n; i++) {
			while (q[i].size())
				q[i].pop();
			vector <int> v;
			for (int j = 0; j < p; j++) {
				int a;	cin >> a;
				v.pb(a);
			}
			sort (v.begin(), v.end());
			for (int j = 0; j < p; j++)
				q[i].push(v[j]);
		}

		cout << "Case #" << t << ": " << go () << endl;
	}

	return 0;
}
