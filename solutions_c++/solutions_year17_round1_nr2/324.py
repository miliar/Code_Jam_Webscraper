#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <bitset>

using namespace std;
typedef pair<int, int> Pi;
typedef long long ll;
#define pii Pi
#define pll PL
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) ((int)(x).size())
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> PL;
typedef long double ldouble;

int n, p;

void solve(){
	scanf("%d%d", &n, &p);
	int r[55], A[55][55];
	for(int i=1;i<=n;i++)scanf("%d", r+i);
	double B[55][55] = {};
	for(int i=1;i<=n;i++)for(int j=1;j<=p;j++)scanf("%d", A[i]+j), B[i][j] = (double)A[i][j] / r[i];
	for(int i=1;i<=n;i++)sort(B[i]+1, B[i]+1+p);
	int s[55] = {};
	double EPS = 1e-10;
	for(int i=1;i<=n;i++)s[i] = 1;
	int ans = 0;
	for(int i=1;9*i<=10000000;i++){
		double l = 0.9 * i, r = 1.1 * i;
		int ok = 1;
		for(int i=1;i<=n;i++){
			while(s[i] <= p && B[i][s[i]] < l - EPS)s[i]++;
			if(s[i] <= p && l < B[i][s[i]] + EPS && B[i][s[i]] < r + EPS);
			else ok = 0;
		}
		if(ok){
			ans++;
			for(int i=1;i<=n;i++)s[i]++;
			--i;
		}
		ok = 1;
		for(int i=1;i<=n;i++)if(s[i] > p){ok = 0; break; }
		if(!ok)break;
	}
	printf("%d\n", ans);
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
