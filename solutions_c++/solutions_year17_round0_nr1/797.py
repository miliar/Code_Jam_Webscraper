#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

int T, K;
char s[2000];

int main() {

	scanf("%d\n", &T);

	for(int t = 0; t < T; t++) {

		gets(s);
		char* p = strstr(s, " ");
		sscanf(p+1, "%d", &K);
		*p = '\0';
		int n = strlen(s);
		int count = 0;

		int i = 0;
		while (i + K - 1 < n) {
			if (s[i] == '-') {
				count ++;
				for(int j = i; j < i+K; j++)
					s[j] = (s[j] == '+')? '-' : '+';
			}
			i ++;
		}

		bool flag = true;
		for(int i = 0; i < n; i++)
			if (s[i] == '-')
				flag = false;

		printf("Case #%d: ", t+1);
		if (flag) {
			printf("%d\n", count);
		}
		else {
			printf("IMPOSSIBLE\n");
		}

	}

	return 0;

}