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

const int MAXN = 50;

string mat[MAXN];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	if(!DEBUG) {
		freopen("A.in", "r", stdin);
		freopen("A.out", "w", stdout);
	}
	int t,u=1,n,m;
	cin>>t;
	while(t--) {
		cin>>n>>m;
		forn(i, n)
			cin>>mat[i];

		forn(i, n)
		forn(j, m) {
			if(mat[i][j] == '?') continue;
			int h = i - 1;
			while(h >= 0 && mat[h][j] == '?') mat[h--][j] = mat[i][j];
			h = i + 1;
			while(h < n && mat[h][j] == '?') mat[h++][j] = mat[i][j];
		}

		forn(i, n)
		forn(j, m) {
			if(mat[i][j] == '?') continue;
			int h = j - 1;
			while(h >= 0 && mat[i][h] == '?') mat[i][h--] = mat[i][j];
			h = j + 1;
			while(h < m && mat[i][h] == '?') mat[i][h++] = mat[i][j];
		}

		cout<<"Case #"<<u++<<":"<<endl;
		forn(i, n)
			cout<<mat[i]<<endl;
	}
	return 0;
}
