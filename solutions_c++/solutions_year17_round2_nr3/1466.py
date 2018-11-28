#include <bits/stdc++.h>
#define isNum(c) c<='9' && c>='0'
#define islettre(c) c<='z' && c>='a'
#define isLETTRE(c) c<='Z' && c>='A'
#define MS0(x) memset(x,0,sizeof(x))
#define MS(x,s) memset(x,s,sizeof(x))
#define rep(i,n) for(i=0;i<n;i++)
#define rev(i,n) for(i=n;i>=0;i--)
#define repv(i,v) for(i=0;i<v.size();i++)
#define repa(i,a,n) for(i=a;i<n;i++)
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define NOT_VISITED 0
#define IS_VISITED 1
#define MOD 1000000009
#define COL 100002
#define trMap(c,i) for(map<char,int>::iterator i = (c).begin(); i != (c).end(); i++)
#define trSet(c,i) for(set< pair <int,char> >::iterator i = (c).begin(); i != (c).end(); i++)
#define PB(val) push_back(val)
#define MP(f,s) make_pair(f,s)
#define abs(i) (i<0)?-i:i
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;
const double INF = 1e19;
int N,Q;
int d[101][101];
int s[101];
int e[101];
vector< pair<int,int> > gr[101];
double dp[101][2][101];

double solve(int i, int sp, int tr, int prev){
	if(i == N-1) return 0;
	if(dp[i][1][prev] == INF){
		if(e[i] < d[i][i+1]) dp[i][1][prev] = INF+1;
		dp[i][1][prev] = solve(i+1,s[i],e[i]-d[i][i+1],i) + d[i][i+1]/(double)s[i];
	}
	if(dp[i][0][prev] == INF){
		if(tr < d[i][i+1]) dp[i][0][prev]=INF+1;
		else dp[i][0][prev] = solve(i+1,sp,tr-d[i][i+1],prev) + d[i][i+1]/(double)sp;
	}
	return min(dp[i][1][prev],dp[i][0][prev]);
}

void solve(int t){
	printf("Case #%d: ", t);
	cin >> N >> Q;
	for(int i = 0; i < N; i++){
		cin >> e[i] >> s[i];
	}
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			dp[i][0][j] = dp[i][1][j] = INF;
			cin >> d[i][j];
			if(d[i][j] != -1) gr[i].push_back({j,d[i][j]});
		}
	}
	int a,b;
	cin >> a >> b;
	printf("%.6f\n", solve(0,-1,-1,0));
}

int main(){
	int T,i,j,k;
	cin >> T;
	i = 1;
	while(T--) solve(i++);
}
