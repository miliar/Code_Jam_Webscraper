#include <bits/stdc++.h>

using namespace std;

char compliment(char x) {
	if (x == '+')
		return '-';
	return '+';
}

int main () {
	int test, cnt = 0, k;
	cin >> test;
	while (test--) {
		cnt++;
		printf("Case #%d: ", cnt);
		string x;
		cin >> x >> k;
		int n = x.length();
		int check = 0, ans = 0;
		for (int i = 0; i < n - k + 1; i++) {
			if (x[i] == '+')
				continue;
			ans++;
			for (int j = i; j < i + k; j++)
				x[j] = compliment (x[j]);
		}
		for (int i = min(0, n - k); i < n; i++) 
			if (x[i] == '-')
				check = 1;
		if (check)
			printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}	
	return 0;
}