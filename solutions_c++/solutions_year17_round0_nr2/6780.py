#include <cstdio>
#include <iostream>

using namespace std;

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out","w",stdout);

	int t;

	cin >> t;
	int l = 0;
	while (t--) {
		l++;
		int k;
		char st[100] = { 0 };
		int num[100] = { 0 };
		scanf("%s", st);
		int len = 0;
		for (int i = 0; i < st[i]; i++) {
			num[i] = st[i] - '0';
			len++;
		}

		printf("Case #%d: ", l);
		if (len == 1) {
			printf("%d\n", num[0]);
			continue;
		}

		for (int i = len - 1; i > 0; i--) {
			if (num[i] < num[i - 1]) {
				for (int j = i; j < len; j++)
					num[j] = 9;
				num[i - 1]--;
			}
		}

		for (int i = 0; i < len; i++) {
			if (num[i] != 0)
				printf("%d", num[i]);
		}
		puts("");
	}
	return 0;
}