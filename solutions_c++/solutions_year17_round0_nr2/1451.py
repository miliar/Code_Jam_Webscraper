#include <bits/stdc++.h>
using namespace std;

string solve() {
	string s;
	cin >> s;
	while(true) {
		bool flag = false;
		for(int i = 0; i < s.length()-1; i++) if(s[i] > s[i+1]) {
			s = to_string(stoll(s) - stoll(s.substr(i+1)) - 1);
			flag = true;
			break;
		}
		if(!flag) break;
	}
	return s;
}

int main() {
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) cout << "Case #" << i << ": " << solve() << endl;
}
