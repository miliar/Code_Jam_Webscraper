#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

char a[1005];

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		int K;
		scanf("%s%d", a, &K);
		int N = strlen(a);
		int ans = 0;
		for (int i = 0; i <= N - K; i++)
			if (a[i] == '-') {
				ans++;
				for (int j = i; j < i + K; j++)
					a[j] = '+' + '-' - a[j];
			}
		bool success = true;
		for (int i = N - K + 1; i < N; i++)
			success &= a[i] == '+';
		printf("Case #%d: ", test);
		if (success)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
}