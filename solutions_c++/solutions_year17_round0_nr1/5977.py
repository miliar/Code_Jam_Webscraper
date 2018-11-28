#if 0==0

#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>

using std::vector;
using std::string;

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n;

	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{
		printf("Case #%d: ", i_case);
		char str[2000];
		scanf("%s", str);
		//scanf("%s", str); //space

		int n = 0;
		scanf("%d", &n);

		bool ok = true;
		int k = strlen(str);
		int ans = 0;
		for (int i = 0 ; i < k ; i++) {
			if (str[i] == '-') {
				if (i+n > k) {
					ok = false;
					break;
				}
				ans ++;

				for (int j = i ; j < i + n ; j++)
					if (str[j] == '-') str[j] = '+'; else str[j] = '-';
			}
		}

		if (ok) printf("%d\n", ans); else printf("IMPOSSIBLE\n");
	}

	return 0;
}

#endif
