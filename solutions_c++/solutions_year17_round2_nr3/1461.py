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

const int maxn=110;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int n,Q,e[maxn],s[maxn],a[maxn][maxn];
double f[maxn];
LL d[maxn];

void init(){
	scanf("%d%d",&n,&Q);
	fou(i,1,n) scanf("%d%d",&e[i],&s[i]);
	fou(i,1,n)
		fou(j,1,n) scanf("%d",&a[i][j]);
}

void solve(){
	int st,ed;
	d[1]=0;
	fou(i,2,n) d[i]=d[i-1]+a[i-1][i];
	while (Q--){
		scanf("%d%d",&st,&ed);
		f[1]=0;
		fou(i,2,n){
			f[i]=infLL;
			fou(j,1,i-1){
				if (d[i]-d[j]<=e[j])
					f[i]=min(f[i],f[j]+(double)(d[i]-d[j])/s[j]);
			}
		}
		printf("%.8f",f[n]);
		if (Q) printf(" "); else printf("\n");
	}
}

int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
