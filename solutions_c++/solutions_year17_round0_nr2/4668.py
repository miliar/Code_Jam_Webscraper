# include <cstdio>
# include <cstring>

using namespace std;

const int MAX_N = 2048;

int n;
char s[MAX_N];

void correct (int idx)
{
    if (idx == n)
        return;
    int i;
    if (s[idx] > s[idx + 1])
    {
        s[idx] --;
        for (i = idx + 1; i < n; i ++)
            s[i] = '9';
        correct (idx - 1);
    }
    correct (idx + 1);
}

void solve ()
{
    int i, j, ans = 0;
    scanf ("%s", s);
    n = strlen (s);
    s[n] = '9';

    correct (0);
    for (i = 0; i < n; i ++)
        if (s[i] != '0')
            break;
    for (; i < n; i ++)
        printf ("%c", s[i]);
    printf ("\n");
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
