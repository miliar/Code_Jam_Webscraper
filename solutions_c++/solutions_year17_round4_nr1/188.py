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
const ll mod = 1000000007;
#define P(a) cout<<(a)<<endl;
#define PP(a) cout<<(a)<<' ';
#define FOR(i, a, b)   for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b)  for (int i = (a); i >= (b); --i)
#define REP(i, b)      for (int i =  0 ; i <  (b); ++i)
#define mid ((l+r)/2)
#define lp (p*2)
#define rp (p*2+1)
void PLL(initializer_list<ll> li) {
	for (auto beg = li.begin(); beg != li.end(); beg++) {
		if (beg != li.begin()) cout << ' '; cout << *beg;
	} cout << endl;
}
int t, n, K;
int a[4] = {0};
int dp[101][101][101];
void up(int &a, int b) {
	if(a<b)a=b;
}

int main () {
	cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		cin >> n >> K;
		memset(a, 0, sizeof(a));
		REP(i, n) {
			int x;
			cin >> x;
			a[x%K]++;
		}
		memset(dp, 0, sizeof(dp));
		FOR(i, 0, a[1])
		FOR(j, 0, a[2])
		FOR(k, 0, a[3]) 
		{
			int cnt = i*1+j*2+k*3;
			cnt %= K;
			if (cnt == 0) cnt = 1;
			else cnt = 0;
			int tmp = dp[i][j][k];
			if (i != a[1]) {
				up(dp[i+1][j][k], tmp+cnt);
			}
			if (j != a[2]) up(dp[i][j+1][k], tmp+cnt);
			if (k != a[3]) up(dp[i][j][k+1], tmp+cnt);
		}
		printf("Case #%d: %d\n", ca, dp[a[1]][a[2]][a[3]] + a[0]);
	}
}
