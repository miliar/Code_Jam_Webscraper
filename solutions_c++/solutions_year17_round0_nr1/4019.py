#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;


int main()
{
    int T, Case = 1;
    char s[1005];
    scanf("%d", &T);
    while(T--)
    {
        int k;
        scanf("%s %d", s, &k);
        int n = strlen(s);
        int ret = 0;
        for(int i=0;i<=n-k;i++)
        {
            if(s[i] == '-')
            {
                ret ++;
                for(int j=i;j-i<k;j++)
                {
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        int flag = 1;
        for(int i=0;i<n;i++)
            if(s[i] == '-')
                flag = 0;
        printf("Case #%d: ", Case++);
        if(!flag) printf("IMPOSSIBLE\n");
        else printf("%d\n", ret);
    }
    return 0;
}
