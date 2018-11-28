#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;
char inv(char x) {
	if (x == '+') return '-';
	return '+';
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int cs = 1;cs <= t;++cs) {
		int k,q=0;
		bool is = true;
		string s;
		cin >> s>>k;
		for (int i = 0;i < s.size() - k+1;++i) {
			if (s[i] == '-') {
				for (int j = i;j < i + k;++j) {
					s[j]=inv(s[j]);
				}
				++q;
			}
		}
		for (int i = s.size() - k + 1;i < s.size();++i) {
			if (s[i] == '-') {
				is = false;
				break;
			}
		}
		if (is) {
			cout << "Case #" << cs << ": " << q << endl;
		}else {
			cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}