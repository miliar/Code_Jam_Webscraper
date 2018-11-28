#include<bits/stdc++.h>

using namespace std;

int nr, N, cif[20];

int main ()
{
freopen ("input", "r", stdin);
freopen ("output", "w", stdout);

int Tests;
scanf ("%d\n", &Tests);
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    printf ("Case #%d: ", test_id);
    scanf ("%lld", &N), N ++, nr = 0;
    while (N)
        cif[++nr] = N % 10, N /= 10;
    reverse (cif + 1, cif + nr + 1);
    long long ans = 0LL;
    for (int i=1; i<nr; i++)
        ans = 1LL * ans * 10LL + 9;
    int lst = nr + 1;
    while (cif[lst - 1] == 0) lst --;
    ///de la [lst, nr] am doar 0 si nu pot sa obtin ceva mai mic
    for (int i=lst - 1; i>=1; i--)
    if (cif[i] > 0)
    {
        bool ok = 1;
        for (int j=1; j<i - 1; j++)
            if (cif[j] > cif[j + 1])
            {
                ok = 0;
                break;
            }
        if (i != 1 && cif[i - 1] > cif[i] - 1) ok = 0;
        if (i == 1 && cif[i] - 1 == 0) ok = 0;
        if (ok)
        {
            long long ans2 = 0;
            for (int j=1; j<i; j++)
                ans2 = ans2 * 10LL + cif[j];
            ans2 = ans2 * 10LL + cif[i] - 1;
            for (int j=i + 1; j<=nr; j++)
                ans2 = ans2 * 10LL + 9;
            if (ans2 > ans) ans = ans2;
            break;
        }
    }
    printf ("%lld\n", ans);
}
return 0;
}
