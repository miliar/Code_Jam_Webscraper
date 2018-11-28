#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
using namespace std;

main() {
	freopen("A-large.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	
	int t, c;
	int tc = 1;
	int count;
	char str[1005];
	int i, j;
	scanf("%d", &t);
	while(t--) {
		scanf("%s %d", str, &c);
		count = 0;
		int len = strlen(str);
		for(i = 0; i <= len - c; i++) {
			if(str[i] == '-') {
				count++;
				for(j = i; j < i + c; j++) {
					if(str[j] == '-') str[j] = '+';
					else if(str[j] == '+') str[j] = '-';
				}
			}
		}
		for(i = 0; i < len; i++) {
			//printf("%c", str[i]); 
			if(str[i] == '-') {
				printf("Case #%d: IMPOSSIBLE\n", tc++);
				break;
			}
		}
		if(i == len) {
			printf("Case #%d: %d\n", tc++, count);
		}
	}
}

