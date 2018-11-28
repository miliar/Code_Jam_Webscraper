#include <stack>
#include <iostream>
#include <thread>
#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <unistd.h>
#include <cmath>
#include <set>
#include <queue>

using namespace std;

typedef long long ll;
typedef double dd;
const ll size = 111002;
//const ll mod = 1000000007;
#define P(a) cout<<(a)<<endl;
#define PP(a) cout<<(a)<<' ';
#define REP(i,m) for (int i=0;i<(m);i++)
#define mid ((l+r)/2)
#define lp (p*2)
#define rp (p*2+1)
typedef pair<int, int> pii;
void PLL(initializer_list<ll> li) {
	for (auto beg = li.begin(); beg != li.end(); beg++) {
		if (beg != li.begin()) cout << ' '; cout << *beg;
	} cout << endl;
}
template <typename T> void disp (T val) {cout << val << endl;}
template <typename T> void PRINT(const T& coll, string opt="") {
	cout << opt; for (const auto &elem: coll) cout << elem << ' '; cout << endl;
}

int main () {
	int t, n, m;
	cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		cin >> n >> m;
		int a[55];
		REP(i, n) cin >> a[i];
		multiset<pii> S[55];
		REP(i, n) {
			REP(j, m) {
				int x;
				cin >> x;
				dd p = x / 0.9 / a[i];
				int high = (p + 1e-8);
				p = x / 1.1 / a[i];
				int low = 1 + (int)(p - 1e-8);
				S[i].insert(pii(low, high));
			}
		}
		int ans = 0;
		while (1) {
			int ok = 0;
			REP(i, n) if (S[i].size() == 0) ok = 1;
			if (ok) break;
			int p = 0;
			REP(i, n) {
				if (*S[i].begin() < *S[p].begin()) p = i;
			}
			ok = 1;
			REP(i, n) {
				if (S[i].begin()->first > S[p].begin()->second) ok = 0;
			}
			if (!ok) S[p].erase(S[p].begin());
			else {
				REP(i, n) S[i].erase(S[i].begin());
				ans++;
			}
		}
		printf("Case #%d: %d\n", ca, ans);
	}
}
