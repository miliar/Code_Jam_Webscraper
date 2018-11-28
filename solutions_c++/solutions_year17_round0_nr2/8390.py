#include <iostream>

void B(int cas) {
	char s[20];
	scanf(" %s", s);
	int i, ln = strlen(s), j;
	for (i = 1; i < ln; i++) {
		if (s[i] < s[i - 1]) {
			break;
		}
	}
	for (j = i; j < ln; j++) {
		s[j] = '9';
	}
	bool move = false;
	if (i < ln) {
		for (j = i - 1; j >= 0; j--) {
			s[j] -= 1;
			if (j > 0) {
				if (s[j] < s[j - 1]) {
					s[j] = '9';
				}
				else break;
			}
			else {
				if (s[j] == '0') {
					move = true;
				}
			}
		}
	}
	printf("Case #%d: %s\n", cas, s + move);
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		B(i + 1);
	}
}