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

typedef struct{	int id,val;} QDE;
typedef struct{ int v,w,nxt;} EDGE;
EDGE edge[MAXM];
int head[MAXN],totaledge;		//link of graph
int n,m;
int dist[MAXN];
bool vis[MAXN];
//------------------------------------------------------------
bool operator < (const QDE& a, const QDE& b) {  return a.val > b.val;}
//------------------------------------------------------------
char str[1000+5];
int bits[40];
LL mask = 0xFFFFFFFF;
void flipbit(int k){
	bits[k>>5] ^= (1<< (k&0x1F) );
}
bool getbit(int k){
	return bool ( bits[k>>5] & (1<< (k&0x1F) ));
}
int solve(int n, int k){
	MST(bits,0);
	int count = 0, last = -1;
	FOR(i,0,n) 
		if(str[i]=='-') {
			if(last<0) last = i;
			flipbit(i);
		}
	if(last<0) return 0;
	while(last < n){
	int p = last; 
	int q = last+k;
	if(q>n) return -1;
	count++;
	//printf("%X\n", bits[0]);	
	while(p<q)
		if(!(p&0x1F) && p+32<=q){
			bits[p>>5] ^= mask;
			p += 32;
		}
		else{
			flipbit(p);
			p++;
		}
	//printf("%X\n", bits[0]);	
	while(!getbit(last) && last < n) last++;
	//cout<<":"<<last<<" , "<<getbit(last)<<endl;
	//break;
	}
	return count;
}
int main(){
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int n,k,T;
	SCF(T);
	FOR(cse,0,T){
		scanf("%s%d",str,&k);
		n = strlen(str);
		printf("Case #%d: ",cse+1);
		int res = solve(n,k);
		if(res<0) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
	return 0;
}
/*

3
---+-++- 3
+++++ 4
-+-+- 4
*/
