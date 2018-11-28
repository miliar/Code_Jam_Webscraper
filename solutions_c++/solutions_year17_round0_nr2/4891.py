#include<cstdio>
#include<cstring>
const int maxn = 30;

int main()
{
	int T, kase = 0;
	scanf("%d", &T);

	while(T--) {
		char num[maxn];
		scanf("%s", num);
		int len = strlen(num);

		int cur = 0, i;
		for(i = 1; i < len; i++) {
			if(num[i-1] < num[i]) cur = i;
			if(num[i-1] > num[i]) break;
		}

		printf("Case #%d: ", ++kase);
		if(i == len) printf("%s\n", num);
		else {
			num[cur] -= 1;
			if(num[0] != '0') putchar(num[0]);
			for(int j = 1; j <= cur; j++) printf("%c", num[j]);
			for(int j = cur+1; j < len; j++) putchar('9');
			putchar('\n');
		}
	}

	return 0;
}
