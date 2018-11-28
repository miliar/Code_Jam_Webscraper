#include<bits/stdc++.h>

using namespace std;

typedef long long LL;

int T;
long long N;
char bar[55],foo[55];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lld",&N);
		long long ans;
		for(ans = 1ll;ans<=N;ans=ans*10ll+1){}
		ans /= 10ll;
		sprintf(bar,"%lld",ans);
		int len = strlen(bar);
		for(int i=0;i<len;i++){
			for(char j=bar[i]+1;j<='9';j++){
				strcpy(foo,bar);
				for(int k=i;k<len;k++){
					foo[k] = j;
				}
				long long cand;
				sscanf(foo,"%lld",&cand);
				if (cand <= N){
					strcpy(bar,foo);
				}
			}
		}
		sscanf(bar,"%lld",&ans);
		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}
