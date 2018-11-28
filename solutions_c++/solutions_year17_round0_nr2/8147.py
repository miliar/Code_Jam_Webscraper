#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	int n;
	cin>>n;
	string s;
	int k;
	ll pot[20];
	pot[0]=1;
	for(int i=1;i<20;++i)
		pot[i]=pot[i-1]*10;
	for(int z=1;z<=n;++z){
		cin>>s;
		bool ok=true;
		for(int i=0;i<s.length()-1;++i)
			if(s[i]>s[i+1]) ok=false;
		printf("Case #%d: ",z);
		if(ok){
			cout<<s<<endl;
			continue;
		}
		ll ans=0,cur=0;
		for(int i=0;i<s.length();++i){
			cur+=(s[i]-'0')*pot[s.length()-1-i];
			int prev=i?s[i-1]:0;
			if(s[i]>prev) ans=max(ans,cur-1);
			if(s[i]<prev) break;
		}
		cout<<ans<<endl;
	}
	return 0;
}