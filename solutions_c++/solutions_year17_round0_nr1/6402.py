// Sourav Verma   IPG_2013108   CodeJam 2017

#include <bits/stdc++.h>
using namespace std;


int main(){
	int t; cin>>t;
	for(int ts=1;ts<=t;ts++){
		string s; cin>>s; int k,flg,cnt=0; cin>>k;
		cout<<"Case #"<<ts<<": ";
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				flg=0;
				for(int j=i;(j<(i+k) && (i+k-1)<s.size() && (s.size()-i)>=k);j++){
					(s[j]=='-') ? s[j]='+' : s[j]='-';
					flg=1;
				}
				if(flg==1) cnt++;
			}
		}
		int p=0;
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				p++; break;
			}
		}
		(p==1) ? cout<<"IMPOSSIBLE\n" : cout<<cnt<<"\n";
	}
	return 0;
}
