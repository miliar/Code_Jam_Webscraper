#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char str[30];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%s",str);
        int len = strlen(str);
        for(int i=0; i<len-1; i++)
        {
            if(str[i] > str[i+1])
            {
                str[i]--;
                int j = i-1;
                while(j >= 0 && str[j] > str[j+1])
                {
                    str[j]--;
                    --j;
                }
                for(j += 2; j<len; j++) str[j] = '9';
                break;
            }
        }
        int k = 0;
        while(str[k] == '0') ++k;
        printf("Case #%d: ",cas);
        for(; k<len; k++)
        {
            putchar(str[k]);
        }
        puts("");
    }
    return 0;
}
