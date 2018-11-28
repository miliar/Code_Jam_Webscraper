#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i < (n);i++)
#define range(i,a,b) for(int i = (a);i <= (b);i++)
#define all(A) A.begin(),A.end()
#define pb push_back
#define mp make_pair
#define sz(A) ((int)A.size())
#define vi vector<int>
#define vl vector<long long>
#define vd vector<double>
#define vp vector<pair<int,int> >
#define ll long long
#define pi pair<int,int>
#define popcnt(x) __builtin_popcount(x)
#define LSOne(x) ((x) & (-(x)))
#define xx first
#define yy second
#define PQ priority_queue
#define print(A,t) cerr << #A << ": "; copy(all(A),ostream_iterator<t>(cerr," " )); cerr << endl
#define prp(p) cerr << "(" << (p).first << " ," << (p).second << ")";
#define prArr(A,n,t)  cerr << #A << ": "; copy(A,A + n,ostream_iterator<t>(cerr," " )); cerr << endl
#define PRESTDIO() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define what_is(x) cerr << #x << " is " << x << endl
#define bit_lg(x) (assert(x > 0),__builtin_ffsll(x) - 1)
const double PI = acos(-1);
using namespace std;

int m,n;
char G[50][50];
int row[50],col[50];

void solve(int sx,int ex,int sy,int ey){
	int ctr = 0;
	char ch;
	range(r,sx,ex) range(c,sy,ey) if(G[r][c] != '?') {
		ctr++;
		ch = G[r][c];
	}
	assert(ctr == 1);
	range(r,sx,ex) range(c,sy,ey) G[r][c] = ch;
}

void solve(int s,int e){
	memset(col,0,sizeof col);
	range(r,s,e) loop(i,n) if(G[r][i] != '?') col[i] = 1;
	vi C;
	loop(i,n) if(col[i]) C.pb(i);
	int l = 0;
	for(int i = 0;i < sz(C);i++){
		if(i == sz(C) - 1) solve(s,e,l,n - 1);
		else solve(s,e,l,C[i]);
		l = C[i] + 1;
	}
}

void solve(){
	memset(row,0,sizeof row);
	vi R;
	loop(i,m) {
		loop(j,n) if(G[i][j] != '?') row[i] = 1;
		if(row[i]) R.pb(i);
	}
	//print(R,int);
	int l = 0;
	for(int i = 0;i < sz(R);i++){
		if(i == sz(R) - 1) solve(l,m - 1);
		else solve(l,R[i]);
		l = R[i] + 1;
	}
}

int main(){
	//freopen("logger.out","w",stderr);
	#ifndef ONLINE_JUDGE
	//	freopen("input.in", "r", stdin);
	//	freopen("output.out", "w", stdout);
	#endif
	int T; scanf("%d",&T);
	range(t,1,T){
		scanf("%d %d",&m,&n);
		loop(i,m) scanf("%s",G[i]);
		solve();
		printf("Case #%d:\n",t);
		loop(i,m) puts(G[i]);
	}
	return 0;
}
