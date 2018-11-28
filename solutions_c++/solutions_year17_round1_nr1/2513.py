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

#define FOR(i, b, n)    for(long long int i=b; i<=n; i++)
#define FORR(i, n, b)   for(long long int i=n; i>=b; i--)

#define mem(a,b)        memset(a,b,sizeof(a))


#define f_input  freopen("A-large.in","r",stdin);
#define f_output freopen("A-large.out","w",stdout);

#define sf              scanf
#define pf              printf

#define chk1 printf("hi......1  \n")
#define chk2 printf("hi......2  \n")
#define TEST(i,t)       long long int i,t;scanf("%lld",&t);for(i=1;i<=t;i++)

#define sz 40
char str[sz][sz],x;
long long int AR[sz],AR1[sz];
int main()
{
    f_input;
    f_output;
    long long int a,b,d,y,N,M,r,c;
    TEST(tc,t)
    {
        cin>>r>>c;
        M=0;
        N=0;
        FOR(i,1,r)
        {
            FOR(j,1,c)
            {
                cin>>str[i][j];
                if(str[i][j]!='?' && AR[i]==0)
                {
                    str[i][1]=str[i][j];
                    AR[i]=j;
                }
            }
            if(AR[i]==0)
            {
                N+=1;
                AR1[N]=i;
            }
        }
        FOR(i,1,r)
        {
            FOR(j,1,c)
            {
                if(AR[i]!=0)
                {
                    if(str[i][j]=='?')
                        str[i][j]=str[i][j-1];
                }
                if(AR1[1]!=0)
                {
                    if(str[i][j]=='?')
                        str[i][j]=str[i-1][j];
                }
            }
        }
        if(AR[1]==0)
        {
            FOR(i,1,r)
            {
                if(AR[i]!=0)
                {
                    a=i;
                    break;
                }
            }
            FOR(i,1,N)
            {
                if(i==1)
                {
                    FOR(j,1,c)
                    {
                        str[AR1[1]][j]=str[a][j];
                    }
                }
                else
                {
                    FOR(j,1,c)
                    {
                        str[AR1[i]][j]=str[AR1[i]-1][j];
                    }
                }
            }
        }
        pf("Case #%lld:\n",tc);
        FOR(i,1,r)
        {
            FOR(j,1,c)
            {
                pf("%c",str[i][j]);
            }
            if(tc==t && i==r)
                break;
            pf("\n");
        }
        mem(AR,0);
        mem(AR1,0);
    }
    return 0;
}
