#include <cstdio>
#include <cstring>

int casei, cases, len;
long long n;
char st[33];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%lld", &n);
		sprintf(st, "%lld", n);
		//printf("%s\n", st);
		len = strlen(st);
		
		int last = 0;
		for (int i = 1; i < len; ++i) {
			if (st[i - 1] > st[i]) {
				--st[last];
				for (int j = last + 1; j < len; ++j) st[j] = '9';
				break;
			}
			else if (st[i - 1] < st[i]) {
				last = i;
			}
		}
		
		printf("Case #%d: ", casei);
		for (last = 0; st[last] == '0' && last + 1 < len; ++last) ;
		for (; last < len; ++last) printf("%c", st[last]);
		printf("\n");
	}
	return 0;
}
