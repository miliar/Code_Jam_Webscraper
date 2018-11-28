#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=1010;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

struct node{
	int x,s;
}a[maxn];

int D,n;

void init(){
	scanf("%d%d",&D,&n);
	fou(i,1,n) scanf("%d%d",&a[i].x,&a[i].s);
}

void solve(){
	double ans,now;
	ans=0;
	fou(i,1,n){
		now=(double)(D-a[i].x)/a[i].s;
		if (ans<now) ans=now;
	}
	ans=D/ans;
	printf("%.9f\n",ans);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
