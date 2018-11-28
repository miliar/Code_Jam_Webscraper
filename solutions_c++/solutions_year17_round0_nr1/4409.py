#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
	//ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int l =1;l<=t;l++){
		string s;
		int k;
		cin>>s>>k;
		ll ans=0;
		int n = s.size();
		bool flag =true;
		int i=0;
		while(i<n){
			if(s[i] == '-' and i < n-k+1){
				for(int j=i;j<i+k;j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
					
				}
				ans+=1;
			}	
		else if(s[i] == '-' and i >= n-k+1){
			flag = false;
			break;

		}
		i++;		
	}
		cout<<"Case #"<<l<<": ";
		if(flag)
			cout<<ans<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
}