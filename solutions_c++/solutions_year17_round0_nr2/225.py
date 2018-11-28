#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<lint, lint> pi;

void solve(){
	string s, t;
	cin >> s;
	for(int i=0; i<s.size(); i++){
		string x = t;
		while(x.size() < s.size()) x.push_back(s[i]);
		if(x <= s) t.push_back(s[i]);
		else{
			t.push_back(s[i] - 1);
			while(t.size() < s.size()) t.push_back('9');
			break;
		}
	}
	while(t[0] == '0'){
		t = t.substr(1, t.size() - 1);
	}
	cout << t << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		solve();
	}
}
