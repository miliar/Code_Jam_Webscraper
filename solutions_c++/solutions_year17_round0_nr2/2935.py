#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int cs = 1; cs <= t; ++cs)
	{
		char s[100];
		scanf("%s",s);
		int len = strlen(s);
		for (int i = 1; i < len; ++i)
		{
			if (s[i] < s[i-1]) {
				int cur = i-1;
				for (int j = i; j < len; ++j)
				{
					s[j] = '9';
				}
				while ((cur > 0) && (s[cur-1] == s[cur])) {
					s[cur] = '9';
					cur--;
				}
				s[cur]--;
				if (s[cur] == '0') {
					for (int j = 1; j <= len; ++j)
					{
						s[j - 1] = s[j];
					}
				}
				break;
			}
		}
		printf("Case #%d: ", cs);
		printf("%s\n", s);
	}
	return 0;
}