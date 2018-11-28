#include<bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		string s,ans;cin>>s;
		int n=s.size();
		bool arr[n];
		for(int i=0;i<n;i++){
			if(s[i]=='-')arr[i]=0;
			else if(s[i]=='+')arr[i]=1;
		}
		int k,count=0;cin>>k;
		for(int i=0;i<=n-k;i++){
			if(arr[i]==0){
				count++;
				for(int j=i;j<i+k;j++)arr[j]=1-arr[j];
			}
		}
		ans=to_string(count);
		//for(int i=0;i<n;i++)cout<<arr[i]<<" ";cout<<endl;
		for(int i=n-k;i<n;i++){
			if(arr[i]==0){
				ans="IMPOSSIBLE";
				break;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
