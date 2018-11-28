#include<bits/stdc++.h>

using namespace std;

int N, K, a[1009];
char sir[1009];

int main ()
{
freopen ("input", "r", stdin);
freopen ("output", "w", stdout);

int Tests;
scanf ("%d\n", &Tests);
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    printf ("Case #%d: ", test_id);
    scanf ("%s %d", sir + 1, &K), N = strlen (sir + 1);
    for (int i=1; i<=N; i++)
        a[i] = (sir[i] == '+');
    int ans = 0;
    for (int i=1; i + K - 1 <= N; i++)
        if (!a[i])
        {
            ans ++;
            for (int j=0; j<K; j++)
                a[i + j] ^= 1;
        }
    bool ok = 1;
    for (int i=N - K + 2; i<=N; i++)
        if (!a[i])
        {
            ok = 0;
            break;
        }
    if (ok) printf ("%d\n", ans);
    else printf ("IMPOSSIBLE\n");
}
return 0;
}
