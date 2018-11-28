#include <iostream>

void A(int cas) {
	char s[1010];
	int l, t = 0;
	scanf(" %s%d", s, &l);
	int ln = strlen(s);
	for (int i = 0; i < ln - l + 1; i++) {
		if (s[i] == '-') {
			for (int j = i; j < i + l; j++) {
				s[j] = s[j] == '-' ? '+' : '-';
			}
			t++;
		}
	}
	for (int i = ln - l + 1; i < ln; i++) {
		if (s[i] == '-') {
			printf("Case #%d: IMPOSSIBLE\n", cas);
			return;
		}	
	}
	printf("Case #%d: %d\n", cas, t);
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		A(i);
	}
}