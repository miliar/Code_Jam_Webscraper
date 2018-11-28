#include <bits/stdc++.h>
#define endl '\n'
#define forn(i, n) for(int i=0;i<n;i++)
#define fore(i, a, b) for(int i=a;i<=b;i++)
#define lli long long int
#define pb(a) push_back(a)
#define pii pair<int,int>
#define fi first
#define se second
#define DEBUG 0

using namespace std;

const int MAXN = 1501;

int A[MAXN];
int B[MAXN];
int memo[MAXN][721][2];

int DP(int id,int a,int f) {
	int b = id - a - 1;
	if(a > 720 || b > 720) return 5000;
	if(id == 1441) return 0;
	if(A[id] && f) return 5000;
	if(B[id] && !f) return 5000;
	if(memo[id][a][f] != -1) return memo[id][a][f];
	return memo[id][a][f] = min( DP(id + 1, a, 1) + (f == 0), DP(id + 1, a + 1, 0) + (f == 1));
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	if(!DEBUG) {
		freopen("B.in", "r", stdin);
		freopen("B.out", "w", stdout);
	}
	int t,a,b,n,m;
	int u = 1;
	cin>>t;
	while(t--) {
		cin>>n>>m;
		fill(A, A + MAXN, 0);
		fill(B, B + MAXN, 0);
		forn(i, n) {
			cin>>a>>b;
			forn(i, b) 
				if(i >= a)
					A[i] = 1;
		}
		forn(i, m) {
			cin>>a>>b;
			forn(i, b) 
				if(i >= a)
					B[i] = 1;
		}
		
		forn(i, 1441)
		forn(j, 721)
		forn(h, 2)
			memo[i][j][h] = -1;
	
		int ans;
		if(A[1]) ans = DP(2, 1, 0);
		else if(B[1]) ans = DP(2, 0, 1);
		else ans = min(DP(2, 1, 0), DP(2, 0, 1));
		cout<<"Case #"<<u++<<": "<<ans + (ans & 1)<<endl;

	}
	return 0;
}
