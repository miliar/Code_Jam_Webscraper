#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
#define maxn 1010
int a[maxn],b[maxn],id[maxn];
bool cmp(int x,int y) {
	return a[x]*1ll*b[x]>a[y]*1ll*b[y];
}
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		int n,k;
		scanf("%d%d",&n,&k);
		for (int i=1;i<=n;i++) {
			scanf("%d%d",a+i,b+i);
			id[i]=i;
		}
		sort(id+1,id+1+n,cmp);
		long long ans=0;
		for (int i=1;i<=n;i++) {
			int cnt=1;
			long long sum=a[id[i]]*1ll*a[id[i]]+2ll*a[id[i]]*b[id[i]];
			for (int j=1;j<=n&&cnt<k;j++) {
				if (i==j) continue;
				if (a[id[j]]<=a[id[i]]) {
					cnt++,sum+=2ll*a[id[j]]*b[id[j]];
				}
			}
			if (cnt<k) continue;
			ans = max(sum,ans);
		}
		printf("Case #%d: %.9lf\n",_,ans*1ll*M_PI);
	}
	return 0;
}
