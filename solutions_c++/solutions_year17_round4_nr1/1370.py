#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<map>
#include<cmath>
#define ll long long
using namespace std;
int T,n,p,a[110],c[110],ans;
int main(){
	scanf("%d",&T);
	for (int I=1;I<=T;I++){
		scanf("%d%d",&n,&p);
		memset(c,0,sizeof(c));
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
			c[a[i]%p]++;
		}
		if (p==2){
			ans=c[0]+(c[1]+1)/2;
		}else if (p==3){
			ans=c[0];
			if (c[2]<=c[1]){
				ans+=c[2];
				c[1]-=c[2];
				ans+=(c[1]+2)/3;
			}else{
				ans+=c[1];
				c[2]-=c[1];
				ans+=(c[2]+2)/3;
			}
		}else{
			ans=c[0];
			if (c[3]<=c[1]){
				ans+=c[3];
				c[1]-=c[3];
				c[3]=0;
			}else{
				ans+=c[1];
				c[3]-=c[1];
				c[1]=0;
			}
			ans+=c[2]/2;
			c[2]%=2;
			if (c[2]==1){
				ans++;
				c[3]=c[3]+c[1]-2;
				ans+=(c[3]+3)/4;
			}else{
				ans+=(c[1]+c[3]+3)/4;
			}
		}
		printf("Case #%d: %d\n",I,ans);
	}
    return 0;
}

