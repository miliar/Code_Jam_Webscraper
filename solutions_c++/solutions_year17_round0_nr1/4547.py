#include<bits/stdc++.h>

using namespace std;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int tc;
	cin>>tc;
	
	for(int i = 1;i<=tc;i++){
		string s;
		cin>>s;
		int k,n = s.length();
		cin>>k;
		long long ans = 0;
		for(int j = 0;j<n;j++){
			while(j<n && s[j] == '+'){
				j++;
			}
			if((j+k) <= n){
				ans++;
				for(int gg = j;gg<j+k;gg++){
					if(s[gg] == '+')
					s[gg] = '-';
					else
					s[gg] = '+';
				}
			}
			else if(j == n){
				cout<<"Case #"<<i<<": "<<ans<<"\n";
				break;
			}
			else{
				cout<<"Case #"<<i<<": IMPOSSIBLE\n";
				break;
			}
		}
		
	}
	return 0;
}
