#include <iostream>
#include <string>
using namespace std;
 
bool isGood(string s){
	bool ret=true;
	for(int i=0;i<s.length();i++){
		if(s[i]=='-'){
			ret=false;
			break;
		}
	}
	return ret;
}
 
 
int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		string s;int k;
		cin>>s>>k;
		int ans=0,pos=s.length()-1;
		while(1){
			if(isGood(s)){
				break;
			}
			else{
				while(s[pos]!='-')pos--;
				if(pos<k-1)break;
				else{
					for(int i=pos;i>=(pos-k+1);i--){
						s[i]=(s[i]=='+')?'-':'+';
					}
					ans++;
					pos--;
				}
			}
		}
		if(isGood(s)){
			cout<<"Case #"<<j<<": "<<ans<<endl;
		}
		else{
			cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}