#include <iostream>
#include <cstdio>
using namespace std;
const int maxn = 1010;
char str[maxn];
int K;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        int ans = 0;
        scanf("%s%d",str,&K);
        int len = strlen(str);
        for(int i=0; i<=len-K; i++)
        {
            if(str[i] == '-')
            {
                ans++;
                for(int j=0; j<K; j++)
                {
                    if(str[i+j] == '+') str[i+j] = '-';
                    else str[i+j] = '+';
                }
            }
        }
        bool flag = true;
        for(int i=len-K+1; i<len; i++)
        {
            if(str[i] == '-')
            {
                flag = false;
                break;
            }
        }
        printf("Case #%d: ",cas);
        if(flag) printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
