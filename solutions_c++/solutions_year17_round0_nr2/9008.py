#include <bits/stdc++.h>
#define ll long long
using namespace std;
int t;
ll n, res;
char s[10];

bool check()
{
    int sz = strlen(s);
    for(int i = sz-1; i > 0; i--)
    {
        if (s[i-1] < s[i])
            return 0;
    }
    return 1;
}

void itoa(ll x)
{
    int sz = 0;
    do
    {
        s[sz] = x%10 + '0';
        x /= 10;
        sz++;

    } while(x);

    s[sz] = 0;
}

int main()
{
    scanf("%d", &t);
    for(int it = 1; it <= t; it++)
    {
        scanf("%d", &n);
        for(ll i = n; i >= 1; i--)
        {
            itoa(i);
            if(check())
            {
                res = i;
                break;
            }
        }
        printf("Case #%d: %d\n", it, res);
    }
    return 0;
}
