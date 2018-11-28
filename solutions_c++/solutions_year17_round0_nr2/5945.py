#if 0==0

#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>

using std::vector;
using std::string;

int main()
{
	//freopen("B-small.in", "r", stdin);
	//freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	char str[1000];

	int n;
	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{
		scanf("%s", str);

		int d = strlen(str);

		for (int i = d - 2 ; i >= 0 ; i--) {
			if (str[i] > str[i+1]) {
				for (int j = i+1 ; j < d ; j++) str[j] = '9';
				str[i]--;
			}
		}

		if (str[0] <= '0') {
			for (int i = 0 ; i < d - 1 ; i++) {
				str[i] = str[i+1];
			}

			str[d - 1] = 0;
		}

		printf("Case #%d: ", i_case);
		printf("%s\n", str);
	}

	return 0;
}

#endif
