#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<string> vs;
const int MOD = 1e9 + 7;
const int di[] = { -1,0,1,0 };
const int dj[] = { 0,1,0,-1 };
#define INF 1000000000
#define EPS 0.000001
#define mp make_pair

bool cmp(deque<int> a, deque<int> b) {
	return a[0] < b[0];
}

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		int n, p; cin >> n >> p;
		vector<deque<int>> ing(n, deque<int>(p));
		vi nd(n);
		for (int i = 0; i < n; i++)
			cin >> nd[i];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++)
				cin >> ing[i][j];
			sort(ing[i].begin(), ing[i].end());
		}
		int r = 0;

		bool end = false, w = false;
		int cur = 1;
		while (!end) {
			w = false;
			for (int i = 0; i < n; i++) {
				while (!ing[i].empty() && 0.9 - (ing[i][0] / (double)(cur * nd[i])) > EPS)
					ing[i].pop_front();

				if (ing[i].empty()) {
					end = true;
					break;
				}
				else if ((ing[i][0] / (double)(cur * nd[i])) - 1.1 > EPS) {
					w = true;
					break;
				}
			}

			if (!w && !end) {
				r++;
				for (int i = 0; i < n; i++)
					ing[i].pop_front();
			}
			else cur++;
		}


		cout << "Case #" << ++tt << ": " << r << endl;
	}
	//cin.ignore(), cin.get();
}
