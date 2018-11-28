#include <cstdio>
#include <iostream>
using namespace std;

int main(){
	int t; cin>>t;
	for(int i=1;i<=t;++i){
		string s; cin>>s;
		int k; cin>>k;
		int n=s.size(), ans=0;
		for(int j=0;j<n-k+1;++j)
			if(s[j]=='-'){
				ans++;
				for(int h=0;h<k;++h)
					if(s[j+h]=='-') s[j+h]='+';
					else s[j+h]='-';
			}
		bool ok=0;
		for(int j=n-k+1;j<n;++j)
			if(s[j]=='-'){
				ok=1; break;
			}
		cout<<"Case #"<<i<<": ";
		if(ok) puts("IMPOSSIBLE");
		else cout<<ans<<endl;
	}
	return 0;
}
