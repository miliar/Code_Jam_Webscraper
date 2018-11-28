#include <bits/stdc++.h>

using namespace std;

inline int mpow(int a, int p)
{
    int r = 1;
    while(p)
    {
        if(p & 1)
            r *= a;
        a *= a;
        p >>= 1;
    }
    return r;
}

long long pow10[20];

inline int cif(long long nr, int pos)
{
    return (nr / pow10[pos]) % 10;
}

inline int nrcif(long long nr)
{
    int i;
    for(i = 0; pow10[i] <= nr; i++);
    return i;
}

inline void setcif(long long& a, int pos, int val)
{
    a -= cif(a, pos) * pow10[pos];
    a += val * pow10[pos];
}

inline void clear0(long long& a)
{
    int lg = nrcif(a);
    for(int i = lg - 1; i >= 0; i--)
    {
        if(cif(a, i) == 0)
        {
            a -= a % pow10[i + 1] - 1;
            return;
        }
    }
}

inline bool step(long long& a)
{
    int lg = nrcif(a);
    for(int i = lg - 1; i != 0; i--)
    {
        if(cif(a, i) > cif(a, i - 1))
        {
            a -= (cif(a, i - i) + 1) * pow10[i - i];
            return true;
        }
    }
    return false;
}

int main()
{
    freopen("tidy.in", "r", stdin);
    freopen("tidy.out", "w", stdout);
    int t;
    scanf("%d", &t);
    pow10[0] = 1;
    for(int i = 1; i < 20; i++)
        pow10[i] = pow10[i - 1] * 10;
    for(int ti = 1; ti <= t; ti++)
    {
        printf("Case #%d: ", ti);
        long long a;
        scanf("%lld", &a);
        do
        {
            clear0(a);
        } while(step(a));
        printf("%lld\n", a);
    }
    return 0;
}
