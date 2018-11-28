#include<bits/stdc++.h>
using namespace std;
int n,P;
int a[110],cnt[44];
void solve(){
	scanf("%d%d",&n,&P);
	memset(cnt,0,sizeof cnt);
	for(int i=1;i<=n;i++){
		int x;scanf("%d",&x);
		cnt[x%P]++;
	}
	int ans=0;
	if(P==2){
		ans+=cnt[0]+(cnt[1]+1)/2;
	}else if(P==3){
		ans+=cnt[0];
		int t=min(cnt[1],cnt[2]);
		ans+=t;
		cnt[1]-=t;cnt[2]-=t;
		ans+=(cnt[1]+2)/3;
		ans+=(cnt[2]+2)/3;
	}
	cout<<ans<<endl;
}
int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
