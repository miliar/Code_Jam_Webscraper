#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
const LL mod = 1e9 + 7;
const int N = 1e5 + 5;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, ca = 1;
    char s[20], ans[20];
    scanf("%d", &T);
    while(T--)
    {
        scanf("%s", s);
        int len = strlen(s);
        for (int i = 0; i < len; i++)
        {
            if (i == 0 || s[i] >= s[i - 1])
            {
                continue;
            }
            else
            {
                for(int j = i - 1; j >= 0; j--)
                {
                    if (s[j] != '0')
                    {
                        s[j] --;
                        for(int k = j + 1; k < len; k++)
                        {
                            s[k] = '9';
                        }
                        i = j - 2;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ", ca++);
        for(int i = 0; i < len; i++)
        {
            if (s[i] != '0')
            {
                for(int j = i; j < len; j++)
                {
                    printf("%c", s[j]);
                }
                break;
            }
        }
        puts("");
    }
    return 0;
}
