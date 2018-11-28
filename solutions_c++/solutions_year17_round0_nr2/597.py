#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

const int MaxN = 20;
int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int t = 1; t <= T; t++)
    {
        char str[MaxN];
        char ret[MaxN];
        memset(str, 0 , sizeof(ret));
        memset(ret, 0 , sizeof(ret));
        scanf("%s", str);
        int n = strlen(str);
        for (int i = 0; i < n; i++)
            ret[i] = str[i];
        int j = 0;
        for (int i = 1; i < n; i++)
        {
            if (str[i] > str[i-1])
            {
                j = i;
            }
            if (str[i] < str[i-1])
            {
                ret[j]--;
                for (int k = j + 1; k < n; k++)
                    ret[k] = '9';
                break;
            }
        }
        printf("Case #%d: ", t);
        int leadingZero = 1;
        for (int i = 0; i < n; i++)
        {
            if (!leadingZero || ret[i] != '0')
                printf("%c", ret[i]);
        }
        printf("\n");
    }
    return 0;
}
