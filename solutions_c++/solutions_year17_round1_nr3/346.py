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
		ll h1, a1, h2, a2, b, d;
		cin >> h1 >> a1 >> h2 >> a2 >> b >> d;
		if (a1 >= h2) {
			printf("Case #%d: 1\n", ca);
			continue;	
		}
		dd tmp = 1.0 * h2 / a1;
		if (b > 0) {
			dd tmp2 = sqrt(1.0 * h2 * b) - a1;
			tmp2 /= b;
			for (int i = tmp2-10; i < tmp2+10; i++) {
				if (i > 0) {
					tmp = min(tmp, i + 1.0 * h2 / (a1 + i * b));
				}
			}
		}
		int turn = 1 + (int)(tmp-1e-8);
		int ans =1000000;
		if (turn == 2 && h1 > a2) ans = 0;
		for (int i = 0; i <= 100; i++) {
			ll aa2 = a2, hh2 = h2, hh1 = h1, aa1 = a1;
			int num = i;
			int ok = 1;
			REP(j, i) {
				ll naa2 = max(0ll, aa2 - d);
				if (hh1 <= naa2) {
					num++;
					hh1 = h1-aa2;
				}
				if (hh1 <= naa2) {
					ok = 0;
					break;
				}
				else {
					hh1 -= naa2;
					aa2 = naa2;
				}
			}
			if (ok == 0) continue;
			//if (ca==2&&i==0)cout<<hh1<<' '<<aa2<<' '<<num<<endl;
			if (aa2 * 2>= h1 || ok == 0) continue;
			REP(i, turn-1) {
				if (hh1 <= aa2) {
					num++;
					hh1 = h1-aa2;
				}
				hh1 -= aa2;
			}
			ans = min(ans, num);
		}
		if (ans == 1000000)
			printf("Case #%d: IMPOSSIBLE\n", ca);
		else 
			printf("Case #%d: %d\n", ca, turn+ans);
	}
}
