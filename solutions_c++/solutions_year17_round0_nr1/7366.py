#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <cstring>
#include <sstream>
#include <map>
#define pi 2*acos (0.0)
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,f,i,l,tc=0,k,n,cnt,j;
    char s[1005];
    scanf("%lld",&t);
    while(t--)
    {
        strcpy(s,"");
        scanf("%s %lld",&s,&k);
        printf("Case #%lld: ",++tc);
        n=strlen(s);
        cnt=0;
        for(i=0;i<=n-k;i++)
            {
                if(s[i]=='-')
                {
                    cnt++;
                    for(j=0;j<k;j++)
                    {
                        if(s[i+j]=='+') s[i+j]='-';
                        else if(s[i+j]=='-') s[i+j]='+';
                    }
                }
            }
            f=0;
        for(i;i<n;i++)
        {
            if(s[i]=='-') f=1;
        }
        if(f==1) printf("IMPOSSIBLE\n");
        else printf("%lld\n",cnt);
    }
    return 0;
}

