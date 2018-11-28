#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

const int MaxN = 1010;
int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int t = 1; t <= T; t++)
    {
        char str[MaxN];
        scanf("%s",str);
        int k;
        scanf("%d",&k);
        int n = strlen(str);
        int ret = 0;
        for (int i = 0; i <= n - k; i++)
        {
            if (str[i] == '-')
            {
                ret += 1;
                for (int j = i; j < i + k; j++)
                {
                    str[j] = (str[j] == '+' ? '-' : '+');
                }
            }
        }
        int flag = 1;
        for (int i = n - k + 1; i < n; i++)
        {
            if (str[i] == '-') flag = 0;
        }
        printf("Case #%d: ", t);
        if (flag) printf("%d\n", ret);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
