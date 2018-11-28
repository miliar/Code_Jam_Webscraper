#include <bits/stdc++.h>

int next(char *s) {
	unsigned int i = 0;
	for (i = 0; i < strlen(s) && s[i] != '-'; i++);
	return i;
}

bool happy(char *s) {
	unsigned int i = 0;
	for (i = 0; i < strlen(s) && s[i] != '-'; i++);
	if (i == strlen(s))
		return true;
	else
		return false;
}

int turn(char *s, int k) {
	int c = 0;
	unsigned int a = 0;

	do {
		if (happy(s)) {
			printf("%d", c);
			return 0;
		}
		a = next(s);
		for (int i = 0; i < k; i++)
			if (s[a+i] == '-')
				s[a+i] = '+';
			else
				s[a+i] = '-';
		c++;
	} while (a < (strlen(s) - k));
	if (happy(s)) {
		printf("%d", c);
		return 0;
	}
	
	printf("IMPOSSIBLE");
	return 0;
}

int main() {
	int t = 0;
	int k = 0;
	char s[1001] = {0};
	
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		memset(s, 0, 1001);
		scanf("%s %d", s, &k);
		printf("Case #%d: ", i + 1);
		turn(s, k);
		printf("\n");
	}
	
	return 0;
}
