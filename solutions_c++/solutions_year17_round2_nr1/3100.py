#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <queue>
#include <map>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORE(i,a,b) for(int i=a;i<=b;i++)
#define SCF(a) scanf("%d",&a)
#define SCFU(a) scanf("%lld",&a)
#define SCF2(a,b) scanf("%d%d",&a,&b)
#define SCF3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define min2(a,b) ((a)<(b))?(a):(b)
#define max2(a,b) ((a)>(b))?(a):(b)
#define MST(a,b) memset(a,b,sizeof(a))
const int INF = 0x3FFFFFFF;
const int N = 1000+5;

typedef long long int LL;
int n,d;
int x[N],v[N];
double solve(){
	double t = 0;
	FOR(i,0,n){
		double ti = (double(d-x[i]))/((double)v[i]);
		t = max(t,ti);
	}
	return d/t;
}
//------------------------------------------------------------
int main(){
	
	freopen("A-large.in","r",stdin);
//	freopen("in.txt","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	SCF(T);
	FOR(cse,0,T){
		SCF2(d,n);
		FOR(i,0,n)	SCF2(x[i],v[i]);
		printf("Case #%d: ",cse+1);
		double ans = solve();
		//cout<<ans<<endl;
		printf("%.6f\n",ans);
	}
	return 0;
}
/*

*/
