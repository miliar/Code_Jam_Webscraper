#include <bits/stdc++.h>
using namespace std;
#define N 1000

int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	int t;cin>>t;
	for(int c=1;c<=t;c++){
		int k;string ss;
		cin>>ss>>k;
		bitset<N+5> bb;
		for(int i=0;i<ss.size();i++)bb[i]=(ss[i]=='+');
		int ans=0;
		for(int i=0;i<=ss.size()-k;i++){
			if(!bb[i]){
				for(int j=0;j<k;j++) bb[j+i]=!bb[j+i];
				ans++;
			}
		}
		bool flag=1;
		for(int i=0;i<ss.size();i++)if(!bb[i]) flag=0;
		if(flag) cout<<"Case #"<<c<<": "<<ans<<'\n';
		else cout<<"Case #"<<c<<": "<<"IMPOSSIBLE\n";
	}
	return 0;
}