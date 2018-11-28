#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("la.txt","r",stdin);
	freopen("ou1.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	int cnt=1;
	while(testcase--){
		string s;
		int k;
		cin>>s;
		cin>>k;
		int ans=0;
		for(int i=0;i<(s.size()-k+1);++i){
			if(s[i]=='-'){
				++ans;
				for(int j=0;j<k;++j){
					if(s[i+j]=='-'){
						s[i+j]='+';
					}
					else{
						s[i+j]='-';
					}
				}
			}
		}
		int res=0;
		for(int i=0;i<s.size();++i){
			if(s[i]=='-'){
				res=1;
				break;
			}
		}
		if(res){
			cout<<"Case #"<<cnt++<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else{
			cout<<"Case #"<<cnt++<<": "<<ans<<"\n";
		}

	}
	return 0;
}