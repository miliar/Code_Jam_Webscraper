#include <bits/stdc++.h>

using namespace std;

int main(){
	string s;
	int t,i,j;
	cin>>t;
	for(int p=1; p<=t; p++){
		cin>>s;
		for(i=1; i<s.size(); i++){
			if(s[i]-'0'<s[i-1]-'0'){
				for(j=i-1; j>=0; j--){
					if(s[j]-'0'>0 && s[j]-1>=s[j-1]) {
						s[j]=s[j]-1;
						for(int k=j+1; k<s.size(); k++) s[k]='9';
						break;
					}
					
				}
			}
		}
		if(s[0]!='0') cout<<"Case #"<<p<<": "<<s<<"\n";
		else {
			cout<<"Case #"<<p<<": ";
			for(int i=1; i<s.size(); i++) cout<<s[i];
			cout<<"\n";
		}
	}
}
