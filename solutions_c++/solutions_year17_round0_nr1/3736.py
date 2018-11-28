#include <bits\stdc++.h>
#define RUN_TEST
using namespace std;

bool check_valid(string s) {
	for (int i = 0; i < s.length(); i++) 
		if (s[i] == '-')
			return false;
	return true;
}

int main() {
#ifdef  RUN_TEST
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif //  RUN_TEST
	int n, c = 1;
	scanf("%d", &n);
	while (n--) {
		string str;
		int K, ans = 0;
		cin >> str >> K;
		for (int i = 0; i + K - 1 < str.length(); i++) {
			if (str[i] == '-') {
				ans++;
				for (int j = i; j <= i + K - 1; j++) str[j] = str[j] == '-' ? '+' : '-';
			}
		}
		printf("Case #%d: ", c++);
		if (check_valid(str)) {
			printf("%d", ans);
		}
		else {
			printf("IMPOSSIBLE");
		}
		putchar('\n');
	}
	return 0;
}