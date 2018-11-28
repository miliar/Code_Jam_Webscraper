#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		string s;
		cin>>s;
		int n=s.length();
		if(n==1){cout<<s<<endl;continue;}
		for(int i=n-2;i>=0;i--){
			if(s[i]>s[i+1]){
				for(int j=i+1;j<n;j++){
					s[j]='9';
				}
				s[i]=s[i]-1;
			}
		}
		if(s[0]=='0'){
			string s1;
			for(int i=1;i<s.length();i++){
				s1+=s[i];
			}
			cout<<s1<<endl;
			continue;
		}
		cout<<s<<endl;
		
	}
	return 0;
}