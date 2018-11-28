#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	cin>>T;
	for(int i=0;i<T;i++) {
		string S;
		int K;
		cin>>S>>K;
		int ans=0;
		for(int j=0;j<=S.size()-K;j++) {
			if(S[j]=='+') continue;
			ans++;
			for(int k=0;k<K;k++) {
				if(S[j+k]=='+') S[j+k]='-'; else S[j+k]='+';
			}
		}
		cout<<"Case #"<<(i+1)<<": ";
		bool NG=0;
		for(int i=S.size()-K+1;i<S.size();i++) {
			if(S[i]=='-') NG=1;
		}
		if(NG) cout<<"IMPOSSIBLE"<<endl; else cout<<ans<<endl;
	}
}
