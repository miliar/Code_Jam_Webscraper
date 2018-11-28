#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("outt.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		printf("Case #%d: ",T);
		long long n,ans;
		short digts[19],d=0,idx;
		bool f=1;
		scanf("%lld",&n);
		ans=n;
		while(n){
			digts[d++]=n%10;
			n/=10;
		}
		for(int i=d-1;i>0;i--)
			if(digts[i]>digts[i-1])f=0,idx=i,i=0;
		if(!f){
			ans=0;
			for(int i=d-1;i>idx;i--)
				if(digts[i]==digts[idx])idx=i;
			digts[idx]--;
			for(int i=idx-1;i>=0;i--)digts[i]=9;
			for(int i=d-1;i>=0;i--)
				ans=ans*10+digts[i];
		}
		printf("%lld\n",ans);
	}

}