#include <bits/stdc++.h>
using namespace std;

int in[26];
char out[1005], L[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        int n;
        scanf ("%d", &n);

        for (int i=0; i<6; i++)
            scanf ("%d", in + (L[i] - 'A'));

        char a, b, c;

        if (in['R' - 'A'] >= max(in['Y' - 'A'], in['B' - 'A']))
            a = 'R', b = 'Y', c = 'B';

        if (in['Y' - 'A'] >= max(in['R' - 'A'], in['B' - 'A']))
            a = 'Y', b = 'R', c = 'B';

        if (in['B' - 'A'] >= max(in['R' - 'A'], in['Y' - 'A']))
            a = 'B', b = 'R', c = 'Y';

        printf("Case #%d: ", test);

        if (in[b - 'A'] + in[c - 'A'] < in[a - 'A'])
        {
            printf("IMPOSSIBLE\n");
            continue;
        }

        fill(out, out + n, '0');
        out[n] = '\0';

        for (int i=0; i<in[a - 'A']; i++)
            out[i * 2] = a;

        int i = n-1;

        while (in[b - 'A']--)
        {
            if (out[i] != '0')  i--;
            out[i] = b;
            i -= 2;
        }

        for (int i=0; i<n; i++)
            if (out[i] == '0')
                out[i] = c;

        printf("%s\n", out);
    }
    
    return 0;
}