#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int cs = 1; cs <= t; ++cs)
	{
		char s[2000];
		int k;
		scanf("%s %d",s,&k);
		int len = strlen(s);
		int ans = 0;
		for (int i = 0; i <= len - k; ++i)
		{
			if (s[i] == '-') {
				ans++;
				for (int j = 0; j < k; ++j)
				{
					if (s[i+j] == '-') {
						s[i+j] = '+';
					} else {
						s[i+j] = '-';
					}
				}
			}
		}
		bool bisa = true;
		for (int i = len - k; i < len; ++i)
		{
			if (s[i] != '+') {
				bisa = false;
			}
		}
		// printf("%s\n", s);
		if (bisa) {
			printf("Case #%d: %d\n", cs,ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n",cs);
		}
	}
	return 0;
}