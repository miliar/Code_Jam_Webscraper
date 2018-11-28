#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int t; cin >>t;
	for(int j=1;j<=t;j++){
		string s; cin >>s;
		int len=s.length();
		int index=0;
		while(1){
			if(index==s.length()-1){
				break;
			}
			if(s[index+1] < s[index]){
				break;
			}
			index++;
		}
		if(index < s.length()-1){
			while(s[index]==s[index-1]){
				index--;
			}
			s[index]--;
		}
		for(int i=index+1;i<s.length();i++){
			s[i]='9';
		}

		cout <<"Case #"<<j<<": ";
		int zero=0;
		while(s[zero]=='0'){
			zero++;
		}
		for(int i=zero;i<s.length();i++){
			cout << s[i];
		}
		cout << endl;
		}
	return 0;
}