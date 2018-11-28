#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

const int maxn = 1000 + 5;

pii p[10];
char s[maxn], c[10];

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    int T, cas = 0;
    c[0] = 'R', c[1] = 'Y', c[2] = 'B';
    scanf("%d", &T);
    while(T--)
    {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < 6; ++i) scanf("%d", &p[i].first), p[i].second = i;
        p[1].first = p[2].first, p[2].first = p[4].first;
        sort(p, p + 3);
        printf("Case #%d: ", ++cas);
        if(p[2].first > p[0].first + p[1].first) puts("IMPOSSIBLE");
        else
        {
            for(int i = 0; i < n; i += 2)
            {
                if(p[2].first > 0)
                {
                    s[i] = c[p[2].second];
                    --p[2].first;
                    if(p[1].first >= p[0].first && p[1].first > 0)
                    {
                        s[i + 1] = c[p[1].second];
                        --p[1].first;
                    }
                    else if(p[0].first >= p[1].first && p[0].first > 0)
                    {
                        s[i + 1] = c[p[0].second];
                        --p[0].first;
                    }
                }
                else
                {
                    if(s[i - 1] == c[p[0].second])
                    {
                        s[i] = c[p[1].second];
                        --p[1].first;
                        if(p[0].first > 0)
                        {
                            s[i + 1] = c[p[0].second];
                            --p[0].first;
                        }
                    }
                    else
                    {
                        s[i] = c[p[0].second];
                        --p[0].first;
                        if(p[1].first > 0)
                        {
                            s[i + 1] = c[p[1].second];
                            --p[1].first;
                        }
                    }
                }
            }
            s[n] = 0;
            puts(s);
        }
    }
    return 0;
}
