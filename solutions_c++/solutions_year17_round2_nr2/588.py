#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

int n, r, o, y, g, b, v;
char ans[1001];
int tab[3], cp[3];
char m[3] = {'R', 'Y', 'B'};

bool check(int a, int bb, int c, int tt[3])
{
    int p = 0, gg = 1;
    for(int i = 0; i <= n - 1; i += 2)
    {
        if(tt[a] > 0) ans[i] = m[a], tt[a]--;
        else if(tt[bb] > 0) ans[i] = m[bb], tt[bb]--;
        else if(tt[c] > 0) ans[i] = m[c], tt[c]--;
        p++;
    }
    while(p < n)
    {
        if(tt[a] > 0) ans[gg] = m[a], tt[a]--;
        else if(tt[bb] > 0) ans[gg] = m[bb], tt[bb]--;
        else if(tt[c] > 0) ans[gg] = m[c], tt[c]--;
        gg += 2;
        p++;
    }
    for(int i = 1; i < n; i++)
        if(ans[i] == ans[i - 1]) return false;
    if(ans[0] == ans[n - 1]) return false;
    return true;
}

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        tab[0] = r;
        tab[1] = y;
        tab[2] = b;

        for(int i = 0; i < n; i++) ans[i] = 0;
        cp[0] = tab[0], cp[1] = tab[1], cp[2] = tab[2];
        if(check(0, 1, 2, cp))
        {
            printf("Case #%d: %s\n", t, ans);
            for(int i = 0; i < n; i++) ans[i] = 0;
            continue;
        }

        for(int i = 0; i < n; i++) ans[i] = 0;
        cp[0] = tab[0], cp[1] = tab[1], cp[2] = tab[2];
        if(check(0, 2, 1, cp))
        {
            printf("Case #%d: %s\n", t, ans);
            for(int i = 0; i < n; i++) ans[i] = 0;
            continue;
        }

        for(int i = 0; i < n; i++) ans[i] = 0;
        cp[0] = tab[0], cp[1] = tab[1], cp[2] = tab[2];
        if(check(1, 0, 2, cp))
        {
            printf("Case #%d: %s\n", t, ans);
            for(int i = 0; i < n; i++) ans[i] = 0;
            continue;
        }

        for(int i = 0; i < n; i++) ans[i] = 0;
        cp[0] = tab[0], cp[1] = tab[1], cp[2] = tab[2];
        if(check(1, 2, 0, cp))
        {
            printf("Case #%d: %s\n", t, ans);
            for(int i = 0; i < n; i++) ans[i] = 0;
            continue;
        }

        for(int i = 0; i < n; i++) ans[i] = 0;
        cp[0] = tab[0], cp[1] = tab[1], cp[2] = tab[2];
        if(check(2, 1, 0, cp))
        {
            printf("Case #%d: %s\n", t, ans);
            for(int i = 0; i < n; i++) ans[i] = 0;
            continue;
        }

        for(int i = 0; i < n; i++) ans[i] = 0;
        cp[0] = tab[0], cp[1] = tab[1], cp[2] = tab[2];
        if(check(2, 0, 1, cp))
        {
            printf("Case #%d: %s\n", t, ans);
            for(int i = 0; i < n; i++) ans[i] = 0;
            continue;
        }

        printf("Case #%d: IMPOSSIBLE\n", t);
        for(int i = 0; i < n; i++) ans[i] = 0;
        
    }
    return 0;
}
