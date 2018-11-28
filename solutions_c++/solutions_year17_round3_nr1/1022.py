#define x first
#define y second
#include<bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef pair<double,double> PDD;
PDD s[10000];
int t,n,k;
const double PI=atan2(0.0,-1.0);
inline bool cmp(const PDD &a,const PDD &b){
	return b.x*b.y<a.x*a.y;
}
inline double cir_out(const PDD &d){
	return d.y*d.x*2*PI;
}
inline double circle(const PDD &d){
	return d.x*d.x*PI;
}
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	REP(_,t){
		scanf("%d%d",&n,&k);
		REP(i,n){
			scanf("%lf%lf",&s[i].x,&s[i].y);
		}
		sort(s,s+n,cmp);
		int mi=max_element(s,s+n)-s;
		double ans=0;
		if(mi<k){
			REP(i,k)ans+=cir_out(s[i]);
			ans+=circle(s[mi]);
		}else{
			int mak=max_element(s,s+k)-s;
			double tmd=0;
			REP(i,k)tmd+=cir_out(s[i]);
			tmd+=circle(s[mak]);
			REP(i,k-1)ans+=cir_out(s[i]);
			ans+=cir_out(s[mi])+circle(s[mi]);
			ans=max(ans,tmd);
		}
		printf("Case #%d: %.9f\n",_+1,ans);
	}
}
