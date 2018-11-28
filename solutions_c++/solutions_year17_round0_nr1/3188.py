#include <bits/stdc++.h>

using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tc;
	cin>>tc;
	int kas=1;
	while(tc-->0){
		string t;int k;cin>>t>>k;
		int ans=0;
		for(int i=0;i<=t.size()-k;i++){
			if(t[i]=='-'){
				ans++;
				for(int j=i,ki=0;ki<k;ki++,j++){
					if(t[j]=='+')t[j]='-';
					else t[j]='+';
				}
			}
		}
		cout<<"Case #"<<kas<<": ";
		for(int i=0;i<t.size();i++)if(t[i]=='-')ans=-1;
		if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
		kas++;
	}
	return 0;
}
