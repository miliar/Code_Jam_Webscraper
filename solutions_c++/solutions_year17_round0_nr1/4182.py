#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cas, C = 1;
    scanf("%d", &cas);
    while(cas--)
    {
        char str[1005];
        int L, K;
        scanf(" %s %d", str, &K);
        int flag = 0, ans = 0;
        L = strlen(str);
        for(int i = 0; str[i]; i++)
        {
            //puts(str);
            if(str[i] == '-' && i + K <= L)
            {
                for(int j = 0; j < K; j++)
                {
                    str[i + j] = (str[i + j] == '-' ? '+' : '-');
                }
                ans++;
            }
            else if(str[i] == '-')
                flag = 1;
            //puts(str);
        }
        printf("Case #%d: ", C++);
        if(flag)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
    return 0;
}
