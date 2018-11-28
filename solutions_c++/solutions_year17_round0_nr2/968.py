#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	char dummy;
	// your code goes here
	int tc = 0;
	scanf("%d", &tc);
	scanf("%c", &dummy);
	for (int q = 1; q <= tc; q++) {
		long long number;
		scanf("%lld", &number);
		string s = to_string(number);
		if (s.length() == 1) {
			printf("Case #%d: %lld\n", q, number);
			continue;
		}
		bool flag = false;
		printf("Case #%d: ", q);
		for (int i = 1; i < s.length(); i++) {
				if (s[i] < s[i-1]) {
					char ref = s[i-1];
					int posn = 0;
					for (int j = i-1; j >= 0; j--) {
						if (s[j] == ref) {
						}
						else {
							posn = j+1;
							break;
						}
					}
					s[posn] = s[posn] - 1;
					for (int j = posn + 1; j < s.length(); j++) {
						s[j] = '9';
						flag = true;
					}
					if (flag) {
						break;
					}
				}
		}
		long long val = stoll(s);
		cout << val << endl;
	}
	
	return 0;
}
