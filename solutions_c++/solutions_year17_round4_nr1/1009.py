#include <bits/stdc++.h>
using namespace std;
#define maxn 120

int n,m;
int a[maxn];
int v[5];

int main()
{
	int Case;
	// freopen("A-small.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("AA.out","w",stdout);
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		memset(v,0,sizeof(v));
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
			a[i]%=m;
			v[a[i]]++;
		}
		int ans;
		if (m==2){
			ans=v[0]+v[1]/2+v[1]%2;
		}
		else if (m==3){
			if (v[1]>v[2]) swap(v[1], v[2]);
			v[2]-=v[1];
			ans=v[0]+v[1]+v[2]/3+(v[2]%3>0);
		}
		else{
			if (v[1]>v[3]) swap(v[1], v[3]);
			v[3]-=v[1];
			ans=v[0]+v[1]+v[2]/2+v[3]/4;
			if (v[2]%2==1 && v[3]%4==3){
				ans+=2;
			}
			else if (v[2]%2+v[3]%4>=1){
				ans+=1;
			}
		}
		printf("Case #%d: %d\n",o, ans);
	}
	return 0;
}