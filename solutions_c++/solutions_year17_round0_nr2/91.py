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

string S;
int n;

ll D[20][10][2];

ll dfs(int x, int d, int s, ll now){
	if(D[x][d][s] != -1)return D[x][d][s] ;
	if(x == n)return now;
	int low = d, high = 9;
	if(s)high = S[x] - '0';
	for(int i=high;i>=low;i--){
		int ns = (s && i == high);
		ll t = dfs(x+1, i, ns, now * 10 + i);
		if(t > 0)return D[x][d][s] = t;
	}
	return D[x][d][s] = 0;
}

void solve(){
	cin >> S;
	n = sz(S);
	memset(D, -1, sizeof D);
	cout << dfs(0, 0, 1, 0) << "\n";
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d: ", tc);
		solve();
	}
}
