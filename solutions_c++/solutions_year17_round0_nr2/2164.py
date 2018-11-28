#include <stdio.h>
#include <string.h>
using namespace std;

char s[100];
int len, tr[100][10];

bool check(int pos, int val, bool smaller) {
	if (pos == len)
		return true;
	int last = smaller ? 9 : s[pos] - '0';
	for (int i = last; i >= val; i--)
		if (check(pos + 1, i, (smaller || i != last))) {
			tr[pos][val] = i;
			return true;
		}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tt = 1; tt <= TC; tt++) {
		scanf("%s", s); len = strlen(s);
		check(0, 0, false);
		int val = 0;
		printf("Case #%d: ", tt);
		for (int i = 0; i < len; i++) {
			if (i || tr[i][val])
				putchar(tr[i][val] + '0');
			val = tr[i][val];
		}
		printf("\n");
	}
}