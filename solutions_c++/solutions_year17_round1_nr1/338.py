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
		char ch[30][30];
		for (int i = 0; i < n; i++) {
			cin >> ch[i];
			ch[i][m] = 'A';
		}
		REP(i, n) REP(j, m) {
			if (ch[i][j] != '?') {
				int k = i-1;
				while (k >=0 && ch[k][j]=='?') {
					ch[k][j] = ch[i][j];
					k--;
				}
				k = i+1;
				while (k < n && ch[k][j] == '?') {
					ch[k][j] = ch[i][j];
					k++;
				}
			}
		}
		int flag = 0;
		REP(j, m) {
			if (ch[0][j] != '?') {
				flag = 1;
			}
			else if (flag) {
				REP(i, n) ch[i][j] = ch[i][j-1];
			}
		}
		for (int j = m-1; j >= 0; j--) {
			if (ch[0][j] == '?') {
				REP(i, n) ch[i][j] = ch[i][j+1];
			}
		}
		printf("Case #%d: \n", ca);
		REP(i, n) {
			ch[i][m] = 0;
			cout<<ch[i]<<endl;
		}
	}
}
