#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int t, n, k;
char s[1050];


int complete()
{
    for (int i = 0; s[i]; i++)
        if (s[i] != '+')
            return 0;
    return 1;
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
        memset(s, 0, sizeof s);
        scanf("%s %d\n", s, &k);
        int rez = 0;
        for (int j = 0, t = strlen(s)-k; j <= t; j++) {
            if (s[j] == '+') continue;
            for (int ind = j; ind < j+k; ind++)
                if (s[ind] == '+') s[ind] = '-';
                else s[ind] = '+';
            rez++;
        }
        if (complete())
            printf("Case #%d: %d\n", i, rez);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }

    return 0;
}
