#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	int cnt=1;
	while(testcase--){
		string s;
		cin>>s;
		if(s.size()==1){
			cout<<"Case #"<<cnt++<<": "<<s<<"\n";
		}
		else{
			string ans="";
			for(int i=s.size()-1;i>=0;i--){
				if(i==0 and s[i]=='0');
				else if(i==0 and s[i]!='0'){
					ans+=s[i];
				}
				else if(i!=0 and s[i]<s[i-1]){
					s[i-1]=s[i-1]-1;
					ans+='9';
					for(int j=0;j<ans.size();++j){
						ans[j]='9';
					}
				}
				else{
					ans+=s[i];
				}
			}
			reverse(ans.begin(),ans.end());
			//cout<<ans<<"\n";
			cout<<"Case #"<<cnt++<<": "<<ans<<"\n";
		}
	}
	return 0;
}