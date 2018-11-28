#include<bits/stdc++.h>
using namespace std;
int main(){
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		printf("Case #%d: ",t);
		string s;
		int k;
		cin>>s>>k;
		int n=s.size();
		int ans=0;
		bool flag=true;
		for(int i=0;i<=n-k;i++){
			if(s[i]=='-'){
				for(int j=i;j<i+k;j++){
					if(s[j]=='+')s[j]='-';
					else s[j]='+';
				}
				ans++;
			}
		}
		for(int i=0;i<n;i++){
			if(s[i]=='-'){
				flag=0;
				break;
			}
		}
		if(flag)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE\n";
	}
	return 0;
}