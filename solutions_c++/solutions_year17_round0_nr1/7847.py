#include <bits/stdc++.h>
using namespace std;

string fun() {
	string s;
	int n;
	cin >> s;
	cin >> n;
	int len = s.length();
	int cnt = 0;
	for(int i=0;i < len-n+1; i++) {
		if(s[i] == '+')
			continue;
		else {
			cnt++;
			for(int j=i;j<i+n;j++) {
				s[j] = (s[j] == '+')?'-':'+';
			}
		}
	}
	for(int i=0;i< len; i++) {
		if(s[i] != '+') {
			return "IMPOSSIBLE";
		}
	}
	return to_string(cnt);
}

int main() {
	int n;
	cin >> n;
	for(int i=1;i<=n;i++) {
		cout << "Case #" << i << ": " << fun() << endl;
	}
	return 0;
}