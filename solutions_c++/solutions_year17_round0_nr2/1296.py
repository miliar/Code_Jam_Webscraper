#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

char str[20];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cnt;
    scanf("%d", &cnt);
    for(int c = 1; c <= cnt; ++c)
    {
        int flag = 0;
        scanf("%s", str);
        int len = strlen(str);
        for(int i = 1; i < len; ++i)
        {
            if(str[i] > str[i - 1]) flag = i;
            if(str[i] < str[i - 1])
            {
                if(i == 1 || str[i - 1] == str[i - 2])
                    i = flag + 1;
                for( ; i < len; ++i)
                    str[i] = '9';
                str[flag] -= 1;
                break;
            }
        }
        for(int i = 0; i < len; ++i)
        {
            if(str[i] != '0')
            {
                flag = i;
                break;
            }
        }
        printf("Case #%d: %s\n", c, str + flag);
    }
    return 0;
}
