#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i=(a); i<(b); i++)
#define pb push_back
#define mk make_pair
#define debug(x) cout<<__LINE__<<": "<<#x<<" = "<<x<<endl;
#define all(c) (c).begin(), (c).end()
#define F first
#define S second
#define UNIQUE(c) sort(all(c)); (c).resize(unique(all(c))-c.begin());
#define pi 3.1415926535897932384626433832795028841971

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

const long long LINF = ( (1LL<<60) );
const long double LEPS = LINF;

inline int cmp(double x, double y = 0, double tol = EPS){
	return ((x <= y+tol) ? (x+tol < y) ? -1:0:1); }


string int2str(int x){ stringstream ss; string str; ss << x; ss >> str;  return str; }
int str2int(string str){ stringstream ss; int x; ss << str; ss >> x;  return x; }



int N, K;

pair<long double, long double>  vec[1123];

long double dp[100][100][100];
int seen[100][100][100];
int t;

long double borda(int i, int j){
	long double ret =  pi*(vec[j].first*vec[j].first - vec[i].first*vec[i].first);
//	printf("borda %d %d = %lf\n", i, j, ret);
	return ret;
}

long double lateral(int i){
	long double ret =  vec[i].second * vec[i].first * 2 * pi;
//	printf("lateral %d = %lf\n", i, ret);
	return ret;
}

long double sol(int n, int k, int j){
//	printf("n=%d k=%d j=%d\n", n,k,j);
	if (k == 0) return pi * vec[j].first * vec[j].first;
	if (n == 0) return -INF;
	
	if (seen[n][k][j] == t) return dp[n][k][j];
	seen[n][k][j] = t;
	
	double a = 0, b = 0;
	a = sol(n-1,k,j);
	b = sol(n-1,k-1,n) + lateral(n) + (j==0? 0 : borda(n,j));
	
	return dp[n][k][j] = max(a, b);
}

int main(){

	int tn; cin >> tn;
	for (t = 1; t <= tn; t += 1)
	{
		printf("Case #%d: ", (t));
		// code
		cin >> N >> K;
		for (int i = 1; i <= N; i += 1)
		{
			long double r, h;
			scanf("%LF %LF", &r, &h);
			vec[i] = mk(r,h);
		}
		sort(vec+1, vec+N+1);
/*
		printf("\n");
		for (int i = N+1; i >= 1; i--){
			cout << vec[i].first << " " << vec[i].second <<"\n";
		}
*/
		long double ans = sol(N,K,0);				
		printf("%.8LF\n", ans);
	}
	return 0;
}



