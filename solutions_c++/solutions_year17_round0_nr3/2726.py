#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SCF(a) scanf("%d",&a)
#define SCFU(a) scanf("%lld",&a)
#define SCF2(a,b) scanf("%d%d",&a,&b)
#define SCF3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define min2(a,b) ((a)<(b))?(a):(b)
#define max2(a,b) ((a)>(b))?(a):(b)
#define MST(a,b) memset(a,b,sizeof(a))
const int INF = 0x3FFFFFFF;
const int MAXN = 8000+5;
const int MAXM = 400000+5;

typedef long long int LL;
//------------------------------------------------------------
void print(LL x){
	if(x&1)
		printf("%lld %lld\n",x/2,x/2);
	else
		printf("%lld %lld\n",x/2,x/2-1);
}
int main(){
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	LL n,k;
	SCF(T);
	FOR(cse,0,T){
		scanf("%lld%lld",&n,&k);
		printf("Case #%d: ",cse+1);
		if(k==1){
			print(n);
		}
		else{
			int i = 0;
			FOR(j,0,64) if( (k>>j) & 1) i = j;
			LL root = (1LL<<i) - 1;
			n -= root;
			LL m = n/(root+1);
			LL cnt = n - m*(root+1);
			if(k-root>cnt) print(m);
			else print(m+1); 
		}
	}
	return 0;
}
/*

3
---+-++- 3
+++++ 4
-+-+- 4
*/
