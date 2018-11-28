#include <map>
#include <cstdlib>
#include <cstdio>
#include <cfloat>
#include <vector>
#include <cmath>
using namespace std;


double solve () {
    char s[60];
    char c;

    int n = 0;
    while (1) {
        scanf("%c", &c);
        if (c != '\n')
            s[n++] = c;
        else
            break;
    }
    for (int i = 0; i < n-1; i++) {
        if (s[i+1] < s[i]) {
            int j;
            for (j = i-1; j > 0; j--)
                if (s[j] < s[j+1]) break;
            if (j != 0 || s[0] < s[1]) j++;
            s[j++]--;
            for (; j < n; j++)
                s[j] = '9';
            break;
        }
    }

    for (int i = 0; i < n; i++)
        if (s[i] != '0') printf("%c", s[i]);
    printf("\n");
}

int main () {
	int T;
	scanf("%d", &T);
    char c;
    scanf("%c", &c);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
        solve();
    }

	return 0;
}
