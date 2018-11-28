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
const double pi = acos(-1.0);
typedef long long int LL;
int n,k;
typedef struct{	int r,h; } QDE;
QDE dat[N];

bool operator < (const QDE& a, const QDE& b) {  
if(a.r == b.r)
	return (a.h > b.h);
else 
	return (a.r > b.r);
}
//------------------------------------------------------------
double solve(int i){
	//disk i is maximal
	vector<double> rh;
	FOR(j,i+1,n){
		double c = (double(dat[j].r)) * dat[j].h;
		rh.push_back(-c);
	}
	sort(rh.begin(),rh.end());
	double ans = (double(dat[i].r)) * dat[i].h;
	FOR(j,0,k-1){
		ans -= rh[j];
		//cout<<i<<" "<<-rh[j]<<endl;
	}
	ans *= 2 * pi;
	ans += pi*dat[i].r*dat[i].r;
	return ans;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	SCF(T);
	FOR(cse,0,T){
		SCF2(n,k);
		FOR(i,0,n)
			SCF2(dat[i].r,dat[i].h);
		
		sort(dat,dat+n);
		//FOR(i,0,n)		cout<<dat[i].r<<" "<<dat[i].h<<endl;
		double ans = 0;
		FOR(i,0,n)
			if(n-i>=k){
				double res = solve(i);
				//cout<<i<<" "<<res<<endl;
				ans = max(res,ans);
			}
		printf("Case #%d: ",cse+1);
		//int ans = solve();
		printf("%.7f\n",ans);
	}
	return 0;
}
/*

*/
