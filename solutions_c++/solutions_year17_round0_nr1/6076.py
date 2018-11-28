#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,m;
	string s;
	cin>>t;
	for(int k=1;k<=t;k++) {
		cin>>s>>m;
		int ans=0,l=s.size();
		for(int i=0;i<=l-m;i++) {
			if(s[i]=='-'){ans++;
				for(int j=0;j<m;j++) {
					if(s[i+j]=='-')
						s[i+j]='+';
					else s[i+j]='-';
				}
			}
		}
		for(int i=l-m+1;i<l;i++) {
			if(s[i]=='-') ans=-1;
		}
		if(ans==-1) printf("Case #%d: IMPOSSIBLE\n",k );
		else printf("Case #%d: %d\n",k,ans);
	}
}