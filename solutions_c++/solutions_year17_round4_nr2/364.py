#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = 1010, mod = int(1e9)  + 7;
int T;
int n,m,c;
int p[N], b[N];
int cnt[N][N], mx[N], rc[N], qc[N];


bool check(int k){
	int ost = 0;
	for(int i = n; i > 0; i--){
		int cur = k;
		cur = min(cur, rc[i] + ost);
		ost += rc[i] - cur;
	}
	if(ost > 0) return 0;
	return 1;
}

void get(int k){
    int ans = 0, ost = 0;
    for(int i = n; i > 0; i--){
		int cur = k;
		ans += max(0, rc[i] - cur);
		cur = min(cur, rc[i] + ost);
		ost += rc[i] - cur;
	}
	printf("%d %d\n", k, ans);
}

void solve(){
	scanf("%d%d%d",&n,&c,&m);
	for(int i = 1; i <= m; i++){
		scanf("%d%d",&p[i],&b[i]);
		cnt[p[i]][b[i]]++;
		rc[p[i]]++;
		qc[b[i]]++;
	} 
	int mix = 0;
	for(int i = 1; i <= n; i++){
		mx[i] = 0;
		for(int j = 1; j <= c; j++){
			mx[i] = max(mx[i], cnt[i][j]);
			cnt[i][j] = 0;
			mix = max(mix, qc[j]);
			qc[j] = 0;
		}
	}
	int l = mix - 1, r = m + 1;
	while(r - l > 1){
		int mid = (l + r) / 2;
		if(check(mid)) r = mid;
		else l = mid;
	}
	get(r);
	for(int i = 1; i <= n; i++) rc[i] = 0;
}

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}