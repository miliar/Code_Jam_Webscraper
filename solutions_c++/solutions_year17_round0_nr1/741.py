#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int maxn = 1e3 + 5;

char s[maxn];

int solve(int k)
{
    int ret = 0, len = strlen(s);
    for(int i = 0; i <= len - k; ++i)
    {
        if(s[i] == '-')
        {
            ++ret;
            for(int j = i; j < i + k; ++j) s[j] = s[j] == '+' ? '-' : '+';
        }
    }
    for(int i = len - k; i < len; ++i) if(s[i] == '-') return -1;
    return ret;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        int k;
        scanf("%s%d", s, &k);
        printf("Case #%d: ", ++cas);
        int ans = solve(k);
        if(~ans) printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
