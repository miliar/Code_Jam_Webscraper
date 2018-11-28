#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char str[1024];
int mars[1024];

int main ()
{
    freopen ("file.in", "r", stdin);
    freopen ("file.out", "w", stdout);

    int t;
    scanf ("%d", &t);

    for (int h = 1; h <= t; ++h)
    {
        scanf ("%s", str + 1);

        int k, n = strlen (str + 1);
        scanf ("%d", &k);

        for (int i = 1; i <= n; ++i)
            mars[i] = 0;

        int x = 0, rez = 0;
        for (int i = 1; i <= n; ++i)
        {
            x ^= mars[i];

            if (x)
                if (str[i] == '+') str[i] = '-';
                else str[i] = '+';

            if (str[i] == '-')
            {
                if (i + k - 1 > n)
                {
                    rez = -1;
                    break;
                }

                else str[i] = '+', x ^= 1, mars[i + k] ^= 1, ++rez;
            }
        }

        printf ("Case #%d: ", h);

        if (rez == -1) printf ("IMPOSSIBLE\n");
        else printf ("%d\n", rez);
    }

    return 0;
}
