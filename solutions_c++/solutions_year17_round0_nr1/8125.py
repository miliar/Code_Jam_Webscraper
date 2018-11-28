#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin>>n;
	string s;
	int k;
	for(int z=1;z<=n;++z){
		cin>>s>>k;
		int ans=0;
		for(int i=0;i<s.length()-k+1;++i){
			if(s[i]=='-'){
				for(int j=0;j<k;++j)
					s[i+j]=s[i+j]=='-'?'+':'-';
				++ans;
			}
		}
		for(int i=0;i<s.length();++i)
			if(s[i]=='-') ans=-1;
		printf("Case #%d: ",z);
		if(ans==-1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	
	return 0;
}