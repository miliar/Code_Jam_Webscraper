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
#define mp make_pair
#define x first
#define y second

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("C-large.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		ll n, k; cin >> n >> k;
		ll rp = k;
		ll rsz = 1;
		map<ll, ll> cur, prv;
		cur[n] = 1;
		while (rp > rsz) {
			rp -= rsz, rsz *= 2;
			prv = cur;
			cur.clear();
			for (auto i : prv) {
				if (i.first % 2 == 1)
					cur[i.first / 2] += i.second * 2;
				else {
					cur[i.first / 2] += i.second;
					cur[i.first / 2 - 1] += i.second;
				}
			}
		}

		for (auto i = prev(cur.end());; i--) {
			if (rp <= i->second) {
				n = i->first;
				break;
			}
			else rp -= i->second;
			if (i == cur.begin())
				break;
		}
		cout << "Case #" << ++tt << ": ";
		cout << n / 2 << " ";
		cout << (n % 2 == 0 ? n / 2 - 1 : n / 2) << endl;
	}
	//cin.ignore(), cin.get();
}
