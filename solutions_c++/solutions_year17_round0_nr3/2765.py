#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <map>

#define IN_FILE "C-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

map<ll, ll> bmap;

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		bmap.clear();
		ll n, k;
		cin >> n >> k;
		bmap[n] = 1;
		ll ans = -1;
		for (ll i = 0; i < k;) {
			auto it = bmap.rbegin();
			ll num = it->first - 1;
			ll h1 = num / 2;
			ll h2 = num / 2 + (num & 1);
			bmap[h1] += it->second;
			bmap[h2] += it->second;
			i += it->second;
			if (i >= k) {
				ans = it->first;
				break;
			}
			bmap.erase(it->first);
		}
		ll num = ans - 1;
		ll a1 = num / 2;
		ll a2 = num / 2 + (num & 1);
		cout << "Case #" << tc << ": " << a2 << " " << a1 << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
