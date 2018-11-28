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
typedef tuple<int, int, int, int> t4;
typedef pair<ll, ll> PL;
typedef long double ldouble;

int chk[102][102][102][102];

int Hd, Ad, Hk, Ak, B, D;


queue <t4> que;
void upd(int a, int b, int c, int d, int t){
	if(chk[a][b][c][d] == -1)chk[a][b][c][d] = t + 1, que.push(t4(a, b, c, d));
}

void dfs(int a, int b, int c, int d, int dis){
	if(a > d){
		upd(a-d, b, c-b, d, dis);
		upd(a-d, min(b+B, c), c, d, dis);
	}
	int nd = max(d-D, 0);
	if(a > nd){
		upd(a-nd, b, c, nd, dis);
	}
	if(Hd > d){
		upd(Hd-d, b, c, d, dis);
	}
}

void solve(){
	scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
	memset(chk, -1, sizeof chk);
	while(!que.empty())que.pop();
	que.push(t4(Hd, Ad, Hk, Ak));
	chk[Hd][Ad][Hk][Ak] = 0;
	while(!que.empty()){
		t4 t = que.front(); que.pop();
		int a = get<0>(t);
		int b = get<1>(t);
		int c = get<2>(t);
		int d = get<3>(t);
		int dis = chk[a][b][c][d];
		if(b >= c){
			printf("%d\n", dis + 1);
			return;
		}
		dfs(a, b, c, d, dis);
	}
	puts("IMPOSSIBLE");
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
