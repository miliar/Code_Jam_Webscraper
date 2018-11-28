#pragma warning(disable:4996)
#include<fstream>
#include<cstring>
using namespace std;
int T, n;
char s[22];
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
	int i,j;
	scanf("%s", s);
	n = strlen(s);
	for (i = n - 1; i > 0; i--) {
		if (s[i] < s[i - 1]) {
			s[i - 1] --;
			for (j = i; j < n; j++) s[j] = '9';
		}
	}
	for (i = 0; i < n; i++) if (s[i] != '0') break;
	for (; i < n; i++) printf("%c", s[i]);
	printf("\n");
}