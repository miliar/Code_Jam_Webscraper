
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
	int t;
	ll n, k;
	cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		cin >> n >> k;
		map<ll, ll> M;
		M[n] = 1;
		while (k > 0) {
			auto iter = M.end();
			iter --;
			ll b = iter->second;
			ll a = iter->first;
			a--;
			ll x = min(a/2, a-a/2);
			ll y = max(a/2, a-a/2);
			if (b >= k) {
				printf("Case #%d: %lld %lld\n", ca, y, x);
				break;
			}
			k -= b;
			M[x] += b;
			M[y] += b;
			M.erase(iter);
		}
	}
}
