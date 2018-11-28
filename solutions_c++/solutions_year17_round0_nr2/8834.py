#include <iostream>
#include <string>
using namespace std;
#define sz(v) ((int)v.size())

bool ok(string& s, int& pos){
	for(int i = 0; i < sz(s)-1;i++){
		if(s[i] > s[i+1]){
			pos = i; return false;
		}
	}
	return true;
}

int main(){
	int t; cin >> t;
	for(int tc = 1; tc <=t; tc++){
		cout << "Case #" << tc << ": ";
		string s; cin >> s;
		int pos = -1;
		while(!ok(s,pos)){
			s[pos]--;
			for(int i = pos+1; i < sz(s); i++) s[i] = '9';
		}
		while(s[0] == '0') s.erase(0,1);
		cout << s << endl;
	}
	return 0;
}