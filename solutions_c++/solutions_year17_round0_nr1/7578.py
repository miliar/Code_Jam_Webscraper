#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	cin>>t;
	int cs=1;
	while(t--){
		int k=0;
		string s;
		cin>>s>>k;
		int l = s.length(),cnt=0;
		for(int i=0;i<l;i++){
			//cout<<i<<"--";
			if(s[i]=='-' && (l-i)>=k){
				for(int j=i;j<(i+k);j++){
			//		cout<<j<<" ";
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
				cnt++;
			//	cout<<"\n"<<i<<"-->"<<s<<"\n";
			}
		}
		bool chk = true;
		for(int i=0;i<l;i++){
			if(s[i]=='-'){
				chk=false;
				break;
			}
		}
		if(chk){
			cout<<"Case #"<<cs<<": "<<cnt<<"\n";
		}else{
			cout<<"Case #"<<cs<<": "<<"IMPOSSIBLE\n";
		}
		cs++;
	}	
	return 0;
}