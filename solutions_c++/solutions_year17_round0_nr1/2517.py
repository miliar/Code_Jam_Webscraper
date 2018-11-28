
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
		char ch[1001];
		cin >> ch >> k;
		int n = strlen(ch);
		vector<int> add(n+1, 0);
		int ans = 0, cnt = 0;
		for (int i = 0; i < n; i++) {
			cnt += add[i];
			int flag = 0;
			if (ch[i] == '+') {
				if (cnt%2) flag = 1;
			}
			else if (cnt%2==0) flag = 1;
			if (flag) {
				if (i > n-k) {
					ans = -1;
					break;
				}
				else {
					ans++;
					add[i+k] -= 1;
					cnt++;
				}	
			}
		}
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", ca);
		else 
			printf("Case #%d: %d\n", ca, ans);
	}
}
