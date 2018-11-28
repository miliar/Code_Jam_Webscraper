#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll conv(string s){
	ll n=s.size(), ret=0;
	for(int i=0;i<n;++i)
		ret=ret*10+(s[i]-'0');
	return ret;
}

int main(){
	int t; cin>>t;
	for(int i=1;i<=t;++i){
		string s; cin>>s;
		int sz=s.size(), d=-1;
		for(int j=0;j<sz-1;++j)
			if(s[j]>s[j+1]){
				d=j;
				break;
			}
		if(d!=-1){
			for(int j=d-1;j>=0;j--){
				if(s[j]!=s[d]){
					d=j+1;
					break;
				}
				if(j==0) d=0;
			}
			s[d]=((s[d]-'0')-1)+'0';
			for(int j=d+1;j<sz;++j)
				s[j]='9';
		}
		ll ans=conv(s);
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
