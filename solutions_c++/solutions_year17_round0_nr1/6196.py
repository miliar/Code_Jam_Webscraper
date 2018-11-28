#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int n,t,sv,k;
    long long int ct=0;
    char str[1005];
    scanf("%d",&t);
    sv=t;

    while(t--)
    {
        ct=0;
        scanf("%s",str);
        scanf("%d",&k);

        n=strlen(str);
        int i=0;
        while(i<n)
        {
            if(str[i]=='+')
            i++;
            else
            break;
        }

        if(i==n)
        printf("Case #%d: 0\n",sv-t);
        else
        {
            while(i<n)
            {
                ct++;
                if((i+k-1)>=n)
                {
                    printf("Case #%d: IMPOSSIBLE\n",sv-t);
                    break;
                }
                else
                {
                    for(int j=i;j<i+k;j++)
                    {
                        if(str[j]=='-')
                        str[j]='+';
                        else
                        str[j]='-';
                    }
                    int pt=i;
                    while(pt<n)
                    {
                        if(str[pt]=='+')
                        pt++;
                        else
                        break;
                    }
                    if(pt==n)
                    {
                        printf("Case #%d: %lld\n",sv-t,ct);
                        break;
                    }
                    else
                    i=pt;
                }
            }
        }
    }

    return 0;
}
