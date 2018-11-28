// Problem B. Tidy Numbers
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		char s[100], *ans = s;
		scanf("%s", s);
		int p = 0, done = 1;
		for (int i = 1; s[i]; i++) {
			if (s[i] > s[i - 1] && done) p = i;
			else if (s[i] < s[i - 1]) done = 0;
		}

		if (!done) {
			for (int i = p + 1; s[i]; i++) s[i] = '9';
			if (--s[p] == '0') ans++;
		}

		printf("Case #%d: %s\n", ti, ans);
	}

	return 0;
}
