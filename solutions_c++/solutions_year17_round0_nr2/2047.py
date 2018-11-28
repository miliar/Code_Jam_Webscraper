#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("Bl.out","w",stdout);
    int T,t,sz;
    char s[22],a[22];
    scanf("%d",&T);
    int i,k;
    bool re;
    for(t=1;t<=T;++t)
    {
        scanf("%s",s+1);
        sz = strlen(s+1);
//        a[sz+1] = '9'+1;
        s[0] = '0';
        re = 0;
        for(i=1;i<=sz;++i)
        {
            if(re)
            {
                a[i] = '9';
                continue;
            }

            if(s[i] < s[i-1])
            {
                re = 1;
                a[i] = '9';
                for(k=i-1;k>0&&s[i-1] == s[k];--k)
                {

                    a[k] = '9';
                }
                a[max(k+1,1)] = s[max(k+1,1)] - 1;
            }
            else
            {
                a[i] = s[i];
            }
        }
        a[sz+1] = '\0';
        for(i=1;i<=sz;++i)
        {
            if(a[i] > '0')
                break;
        }
        printf("Case #%d: %s\n",t,a+i);
    }
    return 0;
}
