#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,k;
	string x;
	cin>>t;
	int cse=1;
	while(t--){
		cout<<"Case #"<<cse++<<": ";
		cin>>x>>k;
		int n=x.size();
		bool sw=1;
		int ans=0;
		for(int i=0;i<n;i++){
			if(x[i]=='-'){
				if(n-i>=k){
					ans++;
					for(int j=i,a=0;a<k;a++,j++){
						if(x[j]=='-')x[j]='+';
						else x[j]='-';
					}
				}else{
					sw=0;
					break;
				}
			}
		}
		if(sw)cout<<ans<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
