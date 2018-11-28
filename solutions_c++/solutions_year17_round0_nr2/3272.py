#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 25
#define ll long long
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

int T;

bool bz[maxn][maxn][2];

ll n;

int a[maxn];

bool ok;

void dfs(int wz,int sam,int las,ll now){
	if (ok) return;
	if (bz[wz][las][sam]) return;
	bz[wz][las][sam]=1;
	if (wz==0) {
		printf("%lld\n",now);
		ok=1;
		return;
	}
	fd(i,9,0) {
		if (las>i) continue;
		if (sam && a[wz]<i) continue;
		dfs(wz-1,sam && a[wz]==i,i,now * 10+i);
	}
}

int main(){
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	fo(test,1,T) {
		mem(bz,0);
		mem(a,0);
		ok=0;
		scanf("%lld",&n);
		fo(i,1,20) a[i]=n % 10,n/=10;
		printf("Case #%d: ",test);
		dfs(20,1,0,0);
	}
	return 0;
}
