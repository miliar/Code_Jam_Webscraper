#include <bits/stdc++.h>
using namespace std;

int T,n,m,c,i,j,k;
int p[1111],d[1111],cnt[1111];
bool v[1111];

int o[1111];


int main(){
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++){
		scanf("%d%d%d",&n,&c,&m);
		memset(cnt,0,sizeof(cnt));
		memset(o,0,sizeof(o));
		for(int i=1;i<=m;i++){
			scanf("%d%d",&p[i],&d[i]);
			cnt[d[i]]++;
			o[p[i]]++;
		}

		int ans=0;

		for(int i=1;i<=1000;i++){
			ans=max(ans,cnt[i]);
		}

		int s=0;
		for(int i=1;i<=n;i++){
			s+=o[i];
			int g=(s/i)+(s%i>0);
			
			ans=max(ans,g);
		}
		
		int ans2=0;
		for(int i=1;i<=n;i++){
			if(o[i]>ans){
				ans2+=o[i]-ans;
			}
		}
		printf("Case #%d: %d %d\n",ca,ans,ans2);

	}

	return 0;
}
