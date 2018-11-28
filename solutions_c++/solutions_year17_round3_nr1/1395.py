#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define ri(x) scanf("%d",&x)
#define rd(x) scanf("%lf",&x)
#define rii(x,y) ri(x),ri(y)
#define rdd(x,y) rd(x),rd(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)
#define USE_MATH_DEFINES

typedef long long ll;
typedef vector<int> vi;

const int MAXN=1010;

int N,T,K;
double pi=M_PI;
bool check[MAXN][MAXN];
double dp[MAXN][MAXN],ans;
vector<pair<double,double> > V;

double f(int i, int k) {
	if(k==0 || i==N) return 0;
	if(check[i][k]) return dp[i][k];
	check[i][k]=true;
	dp[i][k]=max(f(i+1,k), f(i+1,k-1)+2*pi*V[i].first*V[i].second);
	return dp[i][k];
}

int main() {
	ri(T);
	FOR(t,1,T+1) {
		V.clear();
		rii(N,K);
		FOR(i,0,N) {
			double r,h;
			rdd(r,h);
			V.pb({r,h});
		}
		ms(check,false);
		ans=0;
		sort(V.begin(), V.end(), greater<pair<double,double> >());
		FOR(i,0,N) ans=max(ans,f(i+1,K-1)+2*pi*V[i].first*V[i].second+pi*V[i].first*V[i].first);
		printf("Case #%d: %.6lf\n",t,ans);
	}
}
