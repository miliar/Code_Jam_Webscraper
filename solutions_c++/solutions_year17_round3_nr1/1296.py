#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 100000 + 10;
const int M = 1000000007;
const double PI = atan(1) * 4;
const int oo = 1000000000;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
#define pb push_back 
#define all(c) (c).begin(),(c).end()
int n,k;
double dp[1002][1002];

vector<pair<int,int> >v, d;

double calc(int u, int d){
	if(d==k)return 0;
	if(u==n)return -1e18;
	double &ret=dp[u][d];
	if(ret==ret)return ret;
	double x=2*PI*v[u].first*v[u].second;
	return ret=max(x+calc(u+1,d+1),calc(u+1,d));
}
int main(){
	#ifndef ONLINE_JUDGE
		freopen("A-large.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	int T;
	cin>>T;
	for(int t=1; t<=T; ++t){
		cin>>n>>k;
		v.clear();
		v.resize(n);
		for(int i=0; i<n; ++i)
			scanf("%d %d", &v[i].first, &v[i].second);
		sort(all(v));
		reverse(all(v));
		double ans=0;
		memset(dp,-1,sizeof(dp));
		for(int i=0; i<n; ++i)
			ans=max(ans, PI*v[i].first*v[i].first + 2*PI*v[i].first*v[i].second + calc(i+1,1));
		printf("Case #%d: %.9lf\n", t, ans);
	}
}


