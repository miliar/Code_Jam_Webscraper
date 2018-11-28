#include <bits/stdc++.h>

using namespace std;

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int t, kase = 1;
	cin >> t;
	string s;
	while(t--) {
		cin >> s;
		int len = s.size();
		if(len == 1) {
			cout << "Case #" << kase++ << ": " << s << endl; 
			continue;
		}
		char last = s[len - 1];
		for(int i = len - 2; i >= 0; i--) {
			if(s[i] > last) {
				s[i]--;
				for(int j = i + 1; j < len; j++) {
					s[j] = '9';
				}
			}
			last = s[i];
		}
		int pos = 0;
		printf("Case #%d: ", kase++);
		while(s[pos] == '0') pos++;
		for(int i = pos; i < s.size(); i++) {
			cout << s[i];
		}
		cout << endl;
	}
	return 0;
}