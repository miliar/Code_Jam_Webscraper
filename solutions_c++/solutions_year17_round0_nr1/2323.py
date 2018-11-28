#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int t;

void proc(int id) {
	char c;
	char str[1000];
	int n = 0, k;
	while ((c = getchar()) != ' ') {
		str[n] = c;
		n++;
	}
	// printf("%c\n", str[0]);
	// n++;
	scanf("%d\n", &k);
	long long ans = 0;
	for (int i = 0; i <= n - k; i++)
		if (str[i] == '-') {
			ans++;
			for (int j = 0; j < k; j++)
				if (str[i + j] == '-')
					str[i + j] = '+';
				else str[i + j] = '-';
		}
	for (int i = n - k; i < n; i++)
		if (str[i] == '-') {
			printf("Case #%d: IMPOSSIBLE\n", id);
			return;
		}
	printf("Case #%d: %d\n", id, ans);
}

int main() {
	scanf("%d\n", &t);

	for (int i = 0; i < t; i++)
		proc(i + 1);

	return 0;
}
