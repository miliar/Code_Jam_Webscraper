#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    char n[25];
    for(int cases=1; cases<=T; cases++)
    {
        scanf("%s", n);
        int len=strlen(n);
        printf("Case #%d: ", cases);
        int t=0;
        while(t<len-1&&n[t]<=n[t+1])t++;
        if(t==len-1)
        {
            printf("%s\n",n);
            continue;
        }
        n[t]--;
        t--;
        while(t>=0)
        {
            if(n[t]>n[t+1])
            {
                n[t]--;
                t--;
            }
            else
            {
                break;
            }
        }
        fill(n+t+2,n+len,'9');
        if(n[0]=='0')printf("%s\n",n+1);
        else printf("%s\n",n);
    }
    return 0;
}
