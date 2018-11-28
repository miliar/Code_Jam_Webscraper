#include <bits/stdc++.h>
using namespace std;

int a[1005];

int T,len,k,ans;

bool ok;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++) {
		len=0;
		ans=0;
		ok=1;
		char c=getchar();
		while (c!='-' && c!='+') c=getchar();
		while (c=='-' || c=='+') {
			++len;
			a[len]=c=='-' ? 0 : 1;
			c=getchar();
		}
		cin>>k;
		for(int i=1;i<=len-k+1;i++) {
			if (a[i]) continue;
			ans++;
			for(int j=1;j<=k;j++) a[i+j-1]=1-a[i+j-1];
		}
		cout<<"Case #"<<t<<": ";
		for(int i=1;i<=len;i++) 
			if (a[i]==0) {
				ok=0;
				break;
			}
		if (!ok) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
