#include <iostream>
using namespace std;
void flipper(string &s,int i,int k){
	if(s.length()<(i+k)){
		return;
	}
	for(int j=0;j<k;j++){
		if(s[j+i]=='+'){
			s[j+i]='-';
		}else{
			s[j+i] = '+';
		} 
	}
}

bool all_happy(string &s){
	for(int i =0;i<s.length();i++){
		if(s[i]!='+')return false;
	}
	return true;
}

int main(){
	int t;
	cin>>t;
	int p =0;
	while(t--){
		p++;
		string s;
		cin>>s;
		int k;
		cin>>k;
		int cnt= 0;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				cnt++;
				flipper(s,i,k);
			}
		}
		cout<<"Case #"<<p<<": ";
		if(!all_happy(s)){
			cout<<"IMPOSSIBLE";
		}else{
			cout<<cnt;
		}
		cout<<endl;
	}
}