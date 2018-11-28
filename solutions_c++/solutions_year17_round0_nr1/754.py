#include <cstdio>
#include <cstring>
using namespace std;
int T,n,i,j,K,l,p,ca;char s[11111];int a[11111];

int main(){
	for(scanf("%d",&T);T;T--){
		scanf("%s%d",s+1,&K);
		n=strlen(s+1);
		bool pd=1;int ans=0;
		for(int i=1;i<=n;i++)a[i]=(s[i]=='+');
		for(int i=1;i<=n;i++)
			if(a[i]==0){
				ans++;
				for(int j=0;j<K;j++)
					if(i+j>n)pd=0;
					else a[i+j]^=1;
			}
		printf("Case #%d: ",++ca);
		if(pd)printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	
}