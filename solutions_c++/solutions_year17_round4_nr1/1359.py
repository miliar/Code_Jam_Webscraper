#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int z=1;z<=t;++z){
		int n,p;
		cin>>n>>p;
		int cnt[5];
		memset(cnt,0,sizeof cnt);
		for(int i=0;i<n;++i){
			int x;
			cin>>x;
			++cnt[x%p];
		}
		int ans=0;
		if(p==2) ans=cnt[0]+(cnt[1]+1)/2;
		if(p==3){
			ans=cnt[0];
			ans+=min(cnt[1],cnt[2]);
			int resto=max(cnt[1],cnt[2])-min(cnt[1],cnt[2]);
			ans+=(resto+2)/3;
		}
		if(p==4){
			ans=cnt[0];
			ans+=min(cnt[1],cnt[3]);
			ans+=cnt[2]/2;
			int resto=max(cnt[1],cnt[3])-min(cnt[1],cnt[3]);
			if(cnt[2]%2){
				ans++;
				resto = max(resto-2,0);
			}
			ans+=(resto+3)/4;
		}
		printf("Case #%d: %d\n",z,ans);
	}
}