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

using namespace std;
typedef long long ll;
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) x.begin(), x.end()
typedef pair<int, int> pii;
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef tuple<int, int, int, int> t4;

void solve(){
	int n, c, m; scanf("%d%d%d", &n, &c, &m);
	int A[1010] = {}, W[1010] = {};
	int P[1010] = {}, B[1010] = {};
	for(int i=1;i<=m;i++) scanf("%d%d", P+i, B+i);
	for(int i=1;i<=m;i++) A[B[i]]++, W[P[i]]++;
	for(int i=1;i<=n;i++) W[i] += W[i-1];
	int mx = 0;
	for(int i=1;i<=c;i++) mx = max(mx, A[i]);
	for(int i=1;i<=n;i++) mx = max(mx, (W[i] + i - 1) / i);
	printf("%d ", mx);
	int cnt = 0;
	for(int i=1;i<=n;i++){
		int c = W[i] - W[i-1];
		if(c >= mx) cnt += c - mx;
	}
	printf("%d\n", cnt);
}

int main(){
	int Tc = 1; scanf("%d", &Tc);
	for(int tc=1; tc<=Tc; tc++){
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}

