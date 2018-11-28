/*
	"Why do we fall? So we can learn how to pick ourselves up."
	- Alfred, Batman Begins -
*/

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


FILE *f = fopen("pancake-flipper.txt","w");
int main(){

	int T;
	in(T);
	FOR(t,T){
		char s[1005];
		int x[1005];
		
		scanf("%s",s+1);
		int K;
		in(K);
		
		int N=strlen(s+1);
		FOR(i,N) x[i]=(s[i]=='+')?1:0;
		int ans=0;
		FOR(i,N-K+1){
			if(!x[i]){
				FORU(j,i,min(N,i+K-1)){
					x[j]=x[j]^1;
				}
				ans++;
			}
		}
		
		bool ok=1;
		FOR(i,N) if(!x[i]) ok=0;
		
		if(ok) fprintf(f,"Case #%d: %d\n",t,ans);
		else fprintf(f,"Case #%d: IMPOSSIBLE\n",t);
	}

	return 0;
}





