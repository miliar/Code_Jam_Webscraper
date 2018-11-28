#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
char num[20];
int main()
{
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%s", num);
		printf("Case #%d: ", cas);
		LL ans = 0;
		int len = strlen(num);
		bool flag = true;
		while(flag) {
			flag = false;
			for(int i = 1; i < len; ++i)
				if(num[i - 1] > num[i]) {
					flag = true;
					--num[i - 1];
					for(int j = i; j < len; ++j)
						num[j] = '9';
					break;
				}
		}
		for(int i = 0; i < len; ++i)
			ans = ans * 10 + num[i] - '0';
		printf("%lld\n", ans);
	}
	return 0;
}
