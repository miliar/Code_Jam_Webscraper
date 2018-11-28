#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool ordered(long long i) {
	string s = to_string(i);
	for(int i = 0; i < s.size() - 1; i++)
		if(s[i] > s[i + 1])
			return false;
	return true;
}
string solveamele(string s) {
	auto i = stoll(s);
	while(!ordered(i))
		i--;
	return to_string(i);
}
void solve() {
	string s;
	cin >> s;
	for(int i = s.size() - 1; i > 0; i--) {
		char c = 0;
		for(int j = 0; j < i; j++)
			c = max(c, s[j]);
		if(s[i] < c) {
			for(int j = i; j < s.size(); j++)
				s[j] = '9';
			s = to_string(stoll(s.substr(0, i)) - 1) + s.substr(i);
		}
	}
	int i = 0;
	for(; s[i] == '0'; i++);
	cout << s.substr(i) << '\n';
}
int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}