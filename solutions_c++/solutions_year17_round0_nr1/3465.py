#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

int main(){
	int t;
	cin>>t;
	int x=0;
	while(t--){
		x++;
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=0;
		for(int i=s.size()-1;i>=0;i--){
			if(s[i]=='-' && i>=k-1){
				for(int j=i;j>i-k;j--){
					if(s[j]=='+'){
						s[j]='-';
					}else{
						s[j]='+';
					}
				}
				ans++;
			}else if(s[i]=='-'){
				ans=-1;
				break;
			}
		}
		if(ans==-1){
			cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<x<<": "<<ans<<endl;
		}
	}
	return 0;
}