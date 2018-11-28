#include <bits/stdc++.h>

using namespace std;


int main(){
	//ios::sync_with_stdio(true); cin.tie(0); cout.tie(0);
	int T,k,n,i,j;
	long long int ans;
	string s;
	cin>>T;
	for(int t=1;t<=T;t++){
		ans=0;
		cin>>s>>k;
		n=s.length();
		for(i=0;i<n;i++){
			if(s[i]=='+')continue;
			if(i+k>n)break;
			ans++;
			for(j=i;j<i+k;j++){
				if(s[j]=='+')s[j]='-';
				else s[j]='+';
			}
		}
		/*for(i=n-1;i>=0;i--){
			if(s[i]=='+')continue;
			if(i-k<0)break;
			for(j=i;j>i-k;j--){
				ans++;
				if(s[j]=='+')s[j]='-';
				else s[j]='+';
			}
			cout<<endl<<"s="<<s<<endl;
		}*/
		for(i=0;i<n;i++){
			if(s[i]=='-')break;
		}
		cout<<"Case #"<<t<<": ";
		if(i!=n)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
}