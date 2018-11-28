#include <cstdio>
#include <cstring>
main()
{
    freopen("B-large.in","r",stdin);
    freopen("B_L.txt","w",stdout);
    int t; scanf("%d",&t);
    char c[22]; bool w;
    for(int it = 1;it <= t;it++)
    {
        scanf(" %s",c);
        for(int i = strlen(c)-1;i > 0;i--)
        {
            if(c[i] - '0' < 0)
            {
                c[i-1]--;
                c[i] += 10;
            }
            if(c[i] - c[i-1] < 0)
            {
                c[i-1]--;
                for(int j = i;j < strlen(c);j++)
                    c[j] = '9';
            }
        }
        w = false;
        printf("Case #%d: ",it);
        for(int i = 0;i < strlen(c);i++)
        {
            if(!w && c[i] == '0') continue;
            printf("%c",c[i]); w = true;
        }
        printf("\n");
    }

}
