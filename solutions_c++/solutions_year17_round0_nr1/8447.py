#include <bits/stdc++.h>
#define INF 1e9 + 7

using namespace std;

int main() {
	int n, sz, mini;
	string str;
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		cin >> str;
		scanf("%d", &sz);
	
		int flip = 0;
		for (int j = 0; j <= str.length() - sz; j++) {
			if (str[j] == '-') {
				for (int k = j; k < j + sz; k++) {
					str[k] = (str[k] == '+') ? '-' : '+';
				}
				flip++;
			}
		}
		
		bool valid = true;
		for (int j = 0; j < str.length(); j++) {
			if (str[j] == '-') {
				valid = false;
			}
		}
		
		if (valid) {
			printf("Case #%d: %d\n", i + 1, flip);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}
	}
}
