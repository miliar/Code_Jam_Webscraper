#include<iostream>
#include<string>
using namespace std;

string s;


int find(){
	if(s.size()==1){
		cout << s << endl;
		return 0;
	}
	int pos;
	for(pos=0;pos<s.size()-1 && s[pos]<=s[pos+1];pos++);
	if(pos==s.size()-1){
		cout << s << endl;
		return 0;
	}
	if(pos==0){
		if(s[0]=='1'){
			for(int i=1;i<s.size();i++) cout << '9';
			cout << endl;
			return 0;
		}
		s[pos]--;
	}
	else{
		s[pos]--;
	}
	for(int i=pos+1;i<s.size();i++) s[i]='9';
	return 1;
}


int main(){
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++){
		cin >> s;
		cout << "Case #" << tt << ": ";
		while(find() == 1);
	}
	return 0;
}
