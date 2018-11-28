#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

int T, n;
char x[100];
char y[100];

bool check(char* x, int p, char ch) {
	for(int i = p; i < strlen(x); i++)
		if (x[i] < ch)
			return false;
		else if (x[i] > ch)
			return true;
	return true;
}

int main() {

	scanf("%d\n", &T);

	for(int tn = 0; tn < T; tn++) {

		memset(x, 0, sizeof(x));
		gets(x);
		n = strlen(x);
		memset(y, 0, sizeof(y));

		int i = 0;
		while (i < n) {
			if (check(x, i, x[i])) {
				y[i] = x[i];
				i ++;
			}
			else {
				y[i] = x[i] - 1;
				for(int j = i+1; j < n; j++)
					y[j] = '9';
				break;
			}
		}

		i = (y[0] == '0')? 1 : 0;
		printf("Case #%d: ", tn+1);
		for(int j = i; j < n; j++)
			printf("%c", y[j]);
		printf("\n");

	}

	return 0;

}