#include <stdio.h>
#include <algorithm>
#include <cstring>

using namespace std;

int main(void)
{
	int test_case = 0;
	long long n, comp_num;
	char strN[20], ans[20];

	//freopen("B-large.in", "r", stdin);
	//freopen("output.txt", "w", stdout);

	scanf("%d", &test_case);
	for (int tc = 1; tc <= test_case; tc++) {
		scanf("%s", strN);
		n = atoll(strN);
	
		int len = strlen(strN);
		for (int i = 0; i < len; i++)
			ans[i] = strN[0];
		ans[len] = '\0';

		int start_num = 0;
		while (true) {
			comp_num = atoll(ans);

			if (comp_num < n) {
				if (ans[start_num] == '9')
					break;
				for (int i = start_num; i < len; i++)
					ans[i] += 1;
			}

			else if (comp_num > n) {
				ans[start_num] -= 1;
				start_num++;
			}
			else
				break;
		}

		printf("Case #%d: %lld\n", tc, atoll(ans));
	}

	return 0;
}