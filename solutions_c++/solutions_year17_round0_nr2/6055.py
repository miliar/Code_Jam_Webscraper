#include<iostream>
using namespace std;
int main(){
	int T;
	string s;
	cin>>T;
	for(int k=1; k<=T; k++){
		cin>>s;
		int len = s.size();
		int ok = 0;
		string ans = "";
		for(int i=1; i<len; i++){
			if(s[i] < s[i-1]){
				ok = i;
				break;
			}
		}
		if(ok){
			do{
				s[ok] = '9';
				s[--ok]--;
			}while(s[ok] < s[ok-1]);
			for(int i=ok+1; i<len; i++) s[i] = '9';
		}
		printf("Case #%d: ", k);
		for(int i=0, out=0; i<len; i++){
			if(s[i] == '0' && !out) continue;
			else out = 1;
			cout<<s[i];
		}
		cout<<endl;
	}
}
