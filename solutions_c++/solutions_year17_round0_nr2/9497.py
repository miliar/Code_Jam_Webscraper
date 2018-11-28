#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("output-B-large.txt", "w", stdout);

    int T, caseNo = 1, a, i, j, k;
    char num[20];

    scanf("%d", &T);

    while (T--) {
        scanf(" %s", num);

        a = strlen(num);
        a -= 1;

        for (i = 1; i <= a; i++) {
            for (j = a - 1; j >= a - i; j--) {
                if (num[j] > num[j + 1]) {
                    num[j] -= 1;

                    for (k = j + 1; k <= a; k++) num[k] = '9';
                }
            }
        }

        for (i = 0; num[i] == '0'; i++);

        printf("Case #%d: ", caseNo++);

        for (j = i; j <= a; j++) printf("%c", num[j]);

        printf("\n");
    }


    return 0;
}
