#include <bits/stdc++.h>
using namespace std;
#define sz(v) ((int)v.size())
#define FOR(i,x,y) for(int (i)=(x);(i)<(y);(i)++)

bool ok(string& s, int& pos){
	FOR(i,0,sz(s)-1){
		if(s[i] > s[i+1]){
			pos = i; 
			return false;
		}
	}
	return true;
}

int main(){
	int t; cin >> t;
	FOR(tc,1,t+1){
		cout << "Case #" << tc << ": ";
		string s; cin >> s;
		int pos = -1;
		while(!ok(s,pos)){
			s[pos]--;
			FOR(i,pos+1,sz(s)) s[i] = '9';
		}
		while(s[0] == '0') s.erase(0,1);
		cout << s << endl;
	}
	return 0;
}