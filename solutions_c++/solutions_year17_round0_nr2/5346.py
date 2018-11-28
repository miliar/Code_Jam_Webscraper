#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

char S[20];

int duyet1(int l) {
    for (int i = 1; i != l; i++) {
        int a = S[i] - '0';
        int b = S[i-1] - '0';

        if (a < b)
            return i;
    }

    return 0;
}

int duyet2(int p) {
    while(p) {
        int a = S[p] - '0';
        int b = S[p-1] - '0';

        if (a-b >= 1)
            return p;
        p--;
    }

    return 0;
}

int main(int argc, char **argv)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
   
    int T;

    scanf("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);

        scanf("%s", S);

        int l = strlen(S);

        if (l == 1) {
            printf("%s\n", S);
            continue;
        }

        int p = duyet1(l);
        if (p == 0) {
            printf("%s\n", S);
            continue;
        }

        int p2 = duyet2(p-1);
        if (p2 == 0 && S[0] == '1') {
            for (int i = 0; i != l-1; i++)
                printf("9");
        } else {
            for (int i = 0; i != p2; i++)
                printf("%c", S[i]);

            printf("%d", S[p2] - '0' - 1);

            for (int i = p2+1; i != l; i ++)
                printf("9");
        }

        printf("\n");
    }

	return 0;
}
