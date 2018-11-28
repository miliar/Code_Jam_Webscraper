#include <cstdio>
#include <cstring>
char pan[1005];
int main() {
	int T,cnt,x,len;
	scanf("%d ", &T);
	for (int i = 1; i <= T;i++) {
		cnt = 0;
		scanf("%s %d", pan, &x);
		len = strlen(pan);
		for (int j = 0; j+x <= len; j++) {
			if (pan[j] == '-') {
				for (int k = 0; k < x; k++)
					if (pan[j + k] == '-') pan[j + k] = '+';
					else pan[j + k] = '-';
					cnt++;
			}
			else continue;
		}
		printf("Case #%d: ", i);
		bool flag = false;
		for (int k = len - x - 1; k < len; k++) 
			if (pan[k] == '-') {
				flag = true;
				break;
			}

		if(!flag) printf("%d\n", cnt);
		else puts("IMPOSSIBLE");
	}
}