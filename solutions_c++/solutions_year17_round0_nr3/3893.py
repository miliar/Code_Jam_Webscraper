# include <iostream>
# include <cstdio>
# include <algorithm>
# include <cmath>
# include <set>
# include <cstring>
# include <string.h>
# include <sstream>
# include <map>
# include <queue>
# include <vector>
 
# define mp make_pair
# define LL long long
# define vi vector<int>
# define pqu priority_queue
# define iasc int,vector<int>,greater<int>
# define LLasc  LL,vector<LL>,greater<LL>
# define ins push_back
# define pii pair<int,int>
# define fi first
# define se second
 
inline void in(int &MAGNUS) {scanf("%d",&MAGNUS);}
inline void out(int MAGNUS) {printf("%d\n",MAGNUS);}
inline void in(int &MAGNUS,int &CLAR) {scanf("%d%d",&MAGNUS,&CLAR);}
inline void out(int MAGNUS,int CLAR) {printf("%d %d\n",MAGNUS,CLAR);}
 
inline void inl(LL &LIV) {scanf("%lld",&LIV);}
inline void inl(LL &LIV,LL &MART) {scanf("%lld%lld",&LIV,&MART);}
inline void outl(LL LIV) {printf("%lld\n",LIV);}
inline void outl(LL LIV, LL MART) {printf("%lld %lld\n",LIV,MART);}
 
# define FORU(a,b,c) for(int a=b; a<=c; a++)
# define FORD(a,b,c) for(int a=b; a>=c; a--)
# define FOR(a,b) for(int a=1; a<=b; a++)
# define RESET(a) memset(a,0,sizeof(a))
# define MEMO(a) memset(a,-1,sizeof(a))
# define ALL(a) (a).begin(),(a).end()
# define RNG(a,b) (a)+1,(a)+(b)+1
# define BSL(a,b) lower_bound(ALL(a),(b))-(a).begin()
# define BSLX(a,b,c) lower_bound((a)+1,(a)+(b)+1,(c))-a
# define BSU(a,b) upper_bound(ALL(a),(b))-(a).begin()
# define BSUX(a,b,c) upper_bound((a)+1,(a)+(b)+1,(c))-a
# define DEBUG puts("this-part-has-been-reach")
 
using namespace std;
 
int N,K;
pii ans[1000005];
FILE *f=fopen("bathroom-stalls.txt","w");
priority_queue<pii> q;
void build(pii now){
	int id=1;
	q.push(now);
	while(id<=K){
		pii x=q.top();
		q.pop();
		ans[id++]=x;
		q.push(mp(x.fi/2,(x.fi-1)/2));
		q.push(mp(x.se/2,(x.se-1)/2));
	}
 
	while(!q.empty()) {
		q.pop();
	}
}
 
int main(){
 
	int T;
	in(T);
	FOR(t,T){
		in(N,K);
		printf("Case #%d: ",t);
		build(mp(N/2,(N-1)/2));		
		printf("%d %d\n",ans[K].fi,ans[K].se);
	}
 
	return 0;
}