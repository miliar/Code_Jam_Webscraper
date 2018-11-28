# include <cstdio>
# include <cstring>

using namespace std;

const int MAX_N = 2048;

int n, k;
char s[MAX_N];

void solve ()
{
    int i, j, ans = 0;
    scanf ("%s %d", s, &k);
    n = strlen (s);
    for (i = 0; i + k - 1 < n; i ++)
    {
        if (s[i] == '-')
        {
            ans ++;
            for (j = i; j <= i + k - 1; j ++)
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
        }
    }
    for (; i < n; i ++)
        if (s[i] == '-')
        {
            printf ("IMPOSSIBLE\n");
            return;
        }

    printf ("%d\n", ans);
}

int main ()
{
    int t, idt;
    scanf ("%d", &t);
    for (idt = 1; idt <= t; idt ++)
    {
        printf ("Case #%d: ", idt);
        solve ();
    }
    return 0;
}
