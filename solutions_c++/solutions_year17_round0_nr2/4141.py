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
        scanf(" %s", str);
        int L = strlen(str);
        int loc, flag = 0;
        printf("Case #%d: ", C++);
        for(int i = 0; i < L - 1; i++)
        {
            if(str[i] > str[i + 1])
            {
                str[i]--;
                loc = i;
                for(int j = i - 1; j >= 0; j--)
                {
                    if(str[j] > str[j + 1])
                    {
                        str[j]--;
                        loc = j;
                    }
                }
                if(str[0] == '0')
                {
                    for(int j = 0; j < L - 1; j++)
                        printf("9");
                    puts("");
                }
                else
                {
                    for(int j = 0; j <= loc; j++)
                        printf("%c", str[j]);
                    for(int j = loc + 1; j < L; j++)
                        printf("9");
                    puts("");
                }
                flag = 1;
                break;
            }
        }
        if(!flag)
            puts(str);
    }
    return 0;
}
