#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld double
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define vll vector<ll >
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1)
#define all(a) (a).begin(), (a).end()
#define print(s) cerr<<#s<<" : ";for(auto i:(s))cerr<<i<<" ";cerr<<"\n";
#define sd(t) scanf("%d",&(t))
#define pd(t) printf("%d\n",(t))
#define endl "\n"
const int N = 1005;
vector<int> pos[N];
int cnt[N];
int main(){
	int t = 1, n, m, c;
	sd(t);
	for(int tt = 1; tt <= t; tt++){
		sd(n), sd(c), sd(m);
		memset(cnt, 0, sizeof cnt);
		rep(i, 1, c + 1) pos[i].clear();
		int p, b;
		rep(i, 1, m + 1){
			sd(p), sd(b);
			pos[b].pb(p);
			cnt[p]++;
		}	
		int k = 0;
		int pre = 0;
		for(int i = 1; i <= n; i++){
			pre += cnt[i];
			k = max(k, (pre - 1) / i + 1);
		}
		for(int i = 1; i <= c; i++) k = max(k, (int)pos[i].size());
		int x = 0;
		for(int i = 1; i <= n; i++) x += min(k, cnt[i]);
		printf("Case #%d: %d %d\n",tt, k, m - x);
	}
}