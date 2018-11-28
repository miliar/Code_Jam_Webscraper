#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

bool check(string s){
	for(size_t i = 0; i < s.size() - 1; i++)
		if(s[i] - '0' > s[i+1] - '0')
			return false;
	return true;
}

string solve(string s){
	while(!check(s)){
		//cout << s << endl;
		int pos = 0;
		for(size_t i = 0; i < s.size() - 1; i++){
			if(s[i] - '0' > s[i+1] - '0'){pos = i + 1;}
		}
		s[pos-1]--;
		for(size_t i = pos; i < s.size(); i++) s[i] = '9';
	}
	while(s[0] == '0'){
		s = s.substr(1, s.size() - 1);
	}
	return s;
}


int main(){

	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	string ans; string s;
	for(int i = 1; i <= T; i++){
		cin >> s;
		ans = solve(s);
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}