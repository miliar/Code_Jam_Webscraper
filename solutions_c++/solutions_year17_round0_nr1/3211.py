#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

const int N = 1e3 + 7;

int n, k;
char s[N];

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf(" %s %d", s + 1, &k);
        n = strlen(s + 1);
        int res = 0, ok = 1;
        for(int i = 1; i <= n - k + 1; i++)
        {
            if(s[i] == '-')
            {
                res++;
                for(int j = i; j < i + k; j++)
                {
                    s[j] == '+' ? s[j] = '-' : s[j] = '+';
                }
            }
        }
        for(int i = n - k + 2; i <= n; i++)
            if(s[i] != '+') ok = 0;
        if(!ok) printf("Case #%d: IMPOSSIBLE\n", t);
        else printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
