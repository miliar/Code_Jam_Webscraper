#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
using namespace std;
int cas,l,t,i;
long long n,tmp,ans;
int dig[30];

int main(){
#ifdef AKAISORA
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		scanf("%I64d",&n);
		printf("Case #%d: ",t);
		tmp=n;
		l=0;
		memset(dig,0,sizeof(dig));
		while(tmp){
			dig[l++]=tmp%10;
			tmp/=10;
		}
		for(i=l-1;i>=1;i--){
			if(dig[i]>dig[i-1])break;
		}
		if(i>=1){
			while(i<l && dig[i]>dig[i-1]){
				dig[i]--;
				for(int j=i-1;j>=0;j--)dig[j]=9;
				i++;
			}
		}
		ans=0;
		for(int j=l-1;j>=0;j--){
			ans=ans*10+dig[j];
		}
		printf("%I64d\n",ans);
	}
	return 0;
}