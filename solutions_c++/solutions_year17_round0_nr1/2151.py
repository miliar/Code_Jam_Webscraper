#include <iostream>
#include <string>
using namespace std;

int go() {
	int k, num = 0;
	string s;
	cin >> s >> k;
	int len = s.length();
	for (int i = 0; i+k <= len; ++i) {
		if (s[i] == '-') {
			++num;
			for (int j = i; j < i+k; ++j) {
				s[j] = s[j]=='-' ? '+' : '-';
			}
		}
	}
	for (int i = len-k; i<len; ++i) {
		if (s[i] == '-') return -1;
	}
	return num;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output1L.txt","w", stdout);
    
	int T, num; cin >> T;
	for (int c = 1; c <= T; ++c) {
		num = go();
		cout << "Case #" << c << ": ";
		if (num < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << num << endl;
	}
}