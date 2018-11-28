#include <cstring>
#include <iostream>
using namespace std;
const int nmax = 18 + 18;

int T;
char a[nmax];
int n;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		memset(a, 0, sizeof(a));
		scanf("%s", a + 1);
		n = strlen(a + 1);
		for (int i = 2; i <= n; ++i) 
			if (a[i] < a[i - 1]) {
				for (int j = i - 1; j > 0; --j)
					if (j == 1 || a[j] - 1 >= a[j - 1]) {
						a[j] -= 1;
						for (int k = j + 1; k <= n; ++k)
							a[k] = '9';
						break;
					}
				break;
			}
		printf("Case #%d: ", cases);
		if (n > 1 && a[1] == '0') 
			printf("%s\n", a + 2);
		else
			printf("%s\n", a + 1);
	}
	return 0;
}
