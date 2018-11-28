#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<cctype>
#include<map>
#include<stack>
#include<cstdlib>
#include<queue>
#include<vector>
#include<algorithm>
#include<bitset>
#include<algorithm>
#include<set>
#include<limits.h>
using  namespace  std;


#define For(i, b, n)    for(LL i=b; i<=n; i++)
#define ForR(i, n, b)   for(LL i=n; i>=b; i--)


// File.
#define f_input  freopen("A-large.in","r",stdin);
#define f_output freopen("A-large.out","w",stdout);
// i/o.
#define sf              scanf
#define pf              printf


#define test(i,t)       LL i,t;scanf("%lld",&t);for(i=1;i<=t;i++)

typedef unsigned int            U;
typedef long int                L;
typedef unsigned long int       LU;
typedef long long int           LL;
typedef unsigned long long int  LLU;
typedef float                   F;
typedef double                  LF;
typedef char                    C;



string str;
int main()
{
    f_input;
    f_output;

    LL n,m,ap,am,c,d,xx,yy,kk;
    test(tt,t)
    {
        cin>>str;
        sf("%lld",&kk);
        n=str.size();
        m=0;
        c=0;
        For(i,0,n-1)
        {
            if(str[i]=='-')
            {
                xx=yy=0;
                if(n-i<kk)
                {
                    ForR(j,n-1,n-kk)
                    {
                        if(str[j]=='-')
                        {
                            str[j]='+';
                            xx+=1;
                        }
                        else
                        {
                            str[j]='-';
                            yy+=1;
                        }
                    }
                    if(yy!=0)
                    {
                        c=1;
                        break;
                    }
                }
                else
                {
                    For(j,i,i+kk-1)
                    {
                        if(str[j]=='-')
                        {
                            str[j]='+';
                        }
                        else
                        {
                            str[j]='-';
                        }
                    }
                }
                if(c==1)
                    break;
                m+=1;
            }
        }
        if(c==1)
            pf("Case #%lld: IMPOSSIBLE\n",tt);
        else
            pf("Case #%lld: %lld\n",tt,m);
    }
    return 0;
}


