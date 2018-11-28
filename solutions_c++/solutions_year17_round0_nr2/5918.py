#include <cstdio>
#include <cstdlib>

char s[27];

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		scanf("%s", s);
		for (bool flag = 0; !flag; ) {
			flag = 1;
			for (int i = 0; s[i + 1] != '\0'; ++i)
				if (s[i] > s[i + 1]) {
					--s[i];
					for (int j = i + 1; s[j] != '\0'; ++j)
						s[j] = '9';
					flag = 0;
					break;
				}
		}
		int st = 0;
		while (s[st] == '0') ++st;
		printf("Case #%d: %s\n", Case, s + st);
	}
	return 0;
}
