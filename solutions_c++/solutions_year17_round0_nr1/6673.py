#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
using namespace std;

int main(){
	int t;cin>>t;
	for(int kase = 1; kase <= t; kase++){
		string str="";
		int k; 
		cin>>str>>k;
		int n = str.length();
		int ans = 0;
		for(int i=0; i<=n-k; i++){
			if(str[i] == '-'){
				ans++;
				for(int j=0; j<k; j++){
					str[i+j] = (str[i+j] == '-')?'+':'-';
				}
			}
		}

		for(int i=0; i<n; i++){
			if(str[i] == '-'){
				ans = -1;break;
				
			}
		}
		if(ans == -1)cout<<"Case #"<<kase<<": IMPOSSIBLE\n";
		else cout<<"Case #"<<kase<<": "<<ans<<endl;
	}
	return 0;
}
