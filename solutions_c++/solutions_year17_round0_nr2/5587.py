#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

LL n;

string toString(LL x) {
	string res = "";
	while (x > 0) {
		char c = (x%10)+'0';
		res = c+res;
		x /= 10;
	}
	return res;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		cin >> n;
		string s = toString(n);
		int len = s.length();
		for (int i = 1; i < len; ++i) {
			int lastp = len;
			for (int j = i; j > 0; --j)
				if (s[j] < s[j-1]) {
					lastp = j;
					s[j] = '9';
					s[j-1] -= 1;
				}
				else break;
			if (lastp < len) {
				for (int j = lastp+1; j < len; ++j) 
					s[j] = '9';
				break;
			}
		}
		while (s.length() > 0 && s[0] == '0') s = s.substr(1);
		printf("Case #%d: %s\n", test, s.c_str());
	}
	return 0;
}