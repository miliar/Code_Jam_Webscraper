#include<cmath>
#include<ctime>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<queue>
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
int c[20];
LL b10(int m){
	LL ans = 1;
	while(m--) ans *= 10;
	return ans;
}
LL solve(LL n){
if(n<10)return n;
int k = 0;
	LL num = n;
	while(num) {
	c[k++] = num%10;
	num /= 10;
	}
	if(k==19)//1000000000000000000
	return n-1;	
int	s = k-1;
	while(s && c[s] <= c[s-1]) s--;
	if(s==0) return n;
	if(c[s]==1) return b10(k-1)-1;
int q = s;
	while(q < k && c[q] == c[q+1]) q++;
	if(q==k) return  c[k-1] * b10(k-1) - 1;
	//k-1,..,q+1
	return (n-n%b10(q) - 1);
}
int main(){
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	LL n;
	SCF(T);
	FOR(cse,0,T){
		SCFU(n);
		cout<<"Case #"<<cse+1<<": "<<solve(n)<<endl;
	}

	return 0;
}
