#include <iostream>
#include <string>

using namespace std;

void solve() {
	string s;
	cin >> s;
	int n = s.size();
	int j = -1;
	for(int i = 1; i < n; i++) {
		if(s[i] < s[i-1]) {
			j = i-1;
			break;
		}
	}
	if(j < 0) {
		cout << s << '\n';
		return;
	}
	while(j > 0 && s[j] == s[j-1]) j--;
	s[j]--;
	for(int i = j+1; i < n; i++) s[i] = '9';
	if(s[0] == '0') s = s.substr(1);
	cout << s << '\n';
}

int main() {
	int _T;
	cin >> _T;
	for(int _i = 1; _i <= _T; _i++) {
		cout << "Case #" << _i << ": ";
		solve();
	}
}
