#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,k,tc=1,i,j,f;
	string s;
	for(cin>>t;tc<=t;++tc){
		cin>>s;
		if(s=="0"){
			cout<<"Case #"<<tc<<": 0\n";
			continue;
		}
		for(i=f=0;i<s.size();++i){
			if(s[i]>=s[i-1]) continue;
			s[i]='9';
			for(j=i-1;j>=0;--j){
				if(s[j]=='0') s[j]='9';
				else{
					s[j]--;
					if(j==0&&s[j]=='0'){
						for(k=1;k<s.size();s[k++]='9');
						break;
					}
					if(j==0||s[j]>=s[j-1]) break;
				}
			}
			for(i=j+1;i<s.size();s[i++]='9');
		}
		for(i=0;s[i]=='0';++i);
		cout<<"Case #"<<tc<<": ";
		for(;i<s.size();cout<<s[i++]);
		cout<<'\n';
	}
}