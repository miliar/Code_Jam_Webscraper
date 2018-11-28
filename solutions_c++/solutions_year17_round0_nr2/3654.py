#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

char s[30];

int getPos(int l)
{
    for (int i = 0; i < l - 1; ++i)
    {
        if (s[i] > s[i + 1])
        {
            return i;
        }
    }
    return -1;
}

long long solve(long long n)
{
    memset(s, 0, sizeof(s));
    sprintf(s, "%lld", n);
    int l = strlen(s);

    int pos = getPos(l);
    if (pos < 0)
        return n;

    for (int i = pos; i >= 0; --i)
    {
        if (s[i] <= s[i + 1])
        {
            break;
        }
        s[i + 1] = '9';
        s[i]--;
    }

    for (int i = pos + 1; i < l; ++i)
        s[i] = '9';

    long long res = 0;
    for (int i = 0; i < l; ++i)
        res = res * 10 + s[i] - '0';
    return res;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tn = 0; tn < t; ++tn)
    {
        long long n;
        cin >> n;
        printf("Case #%d: %lld\n", tn + 1, solve(n));
    }
    return 0;
}