#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

int main(){
	int t;
	cin>>t;
	int x=0;
	while(t--){
		x++;
		lli n;
		cin>>n;
		string s=to_string(n);
		for(int i=0;i<s.size()-1;i++){
			if(s[i]>s[i+1]){
				s[i]=s[i]-1;
				for(int j=i+1;j<s.size();j++){
					s[j]='9';
				}
				i=-1;
			}
		}
		if(s[0]=='0'){
			s=s.substr(1);
		}
		cout<<"Case #"<<x<<": "<<s<<endl;
	}
	return 0;
}