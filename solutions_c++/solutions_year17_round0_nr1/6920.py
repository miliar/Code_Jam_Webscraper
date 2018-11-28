#pragma warning(disable:4996)
#include<fstream>
#include<cstring>
#define N 1002
using namespace std;

int T,n,k;
char s[N];
void process();
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i;

	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		process();
	}
	return 0;
}

void process()
{
	int i, j, cnt = 0;
	scanf("%s", s);
	scanf("%d", &k);
	n = strlen(s);
	for (i = 0; i < n - k + 1; i++) {
		if (s[i] == '-') {
			for (j = i; j < i + k; j++) {
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			cnt++;
		}
	}
	for (i = 0; i < n; i++) {
		if (s[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}

	printf("%d\n", cnt);
}