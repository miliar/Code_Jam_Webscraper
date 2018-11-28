#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int cs = 1;cs <= t;++cs) {
		string s;
		cin >> s;
		int j=s.size();
		for (int i = 0;i < s.size() - 1;++i) {
			if (s[i] > s[i + 1]) {
				j = i;
				while (j>0&&s[j] == s[j-1]) {
					--j;
				}
				break;
			}
		}
		if (j == s.size()) {
			cout << "Case #" << cs << ": " << s << endl;
			continue;
		}
		--s[j];
		for (int i = j + 1;i < s.size();++i) {
			s[i] = '9';
		}
		j = 0;
		while (s[j] == '0') {
			++j;
		}
		s = s.substr(j);
		cout << "Case #" << cs << ": " << s << endl;
	}
	return 0;
}