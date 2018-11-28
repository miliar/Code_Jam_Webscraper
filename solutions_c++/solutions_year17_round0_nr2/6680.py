#include <bits/stdc++.h>
#define MAXL 100010
#define LL long long
using namespace std;
int t;
LL ten[19],n,ans;
int main() {
	//freopen("easy.in","r",stdin);
	//freopen("easy.out","w",stdout);
	scanf("%d",&t);
	ten[0]=1;
	for (int i=1;i<19;i++) ten[i]=ten[i-1]*10+1;
	for (int k=1;k<=t;k++){
		scanf("%lld",&n);
		ans=0;
		for (int j=0;j<9;j++){
			for (int i=18;i>=0;i--)
			if (ans+ten[i]<=n){
				ans+=ten[i];
				break;
			}
		}
		printf("Case #%d: ",k);
		printf("%lld\n",ans);
	}
}
