#include <cstdio>
#include <cstring>

const int N = 1000 + 10;

char string[N];
int n;

void Flip(int pivot) {
	string[pivot] = '+' + '-' - string[pivot];
}

int m;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		scanf("%s", string + 1);
		n = strlen(string + 1);
		scanf("%d", &m);
		bool valid = true;
		int answer = 0;
		for (int i = 1; i <= n; ++i) {
			if (string[i] == '+') continue;
			if (i + m - 1 > n) {
				valid = false;
				break;
			}
			answer++;
			for (int j = i; j <= i + m - 1; ++j) {
				Flip(j);
			}
		}
		printf("Case #%d: ", t);
		if (!valid) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%d\n", answer);
		}
	}
}