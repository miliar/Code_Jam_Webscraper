#include<bits/stdc++.h>
using namespace std;

int getNumBits(int x){
	return __builtin_popcount(x);
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++){
	
		string s;
		cin>>s;
		
		for(int j=s.length()-1;j>0;j--){
			if(s[j]<s[j-1]){
				for(int k=s.length()-1;k>=j;k--){
					s[k]='9';
				}
				s[j-1]=s[j-1]-1;
			}
			
		}
		
		cout<<"Case #"<<i<<": ";
		
		if(s[0]=='0'){
			for(int j=1;j<s.length();j++){
				cout<<s[j];
			}
			cout<<endl;
		}
		else cout<<s<<endl;
	}
	
	return 0;
}
