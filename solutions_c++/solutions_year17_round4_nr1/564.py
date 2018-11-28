#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define MEM(a,x) memset(a,x,sizeof a)
#define eps 1e-8
#define MOD 10009
#define MAXN 10010
#define MAXM 100010
#define INF 99999999
#define ll __int64
#define bug cout<<"here"<<endl
#define fread freopen("A-large.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)

using namespace std;

int n,p;
int g[110];

void solve(int t)
{
    int ans=0;
    if(p==2)
    {
        int one=0;
        for(int i=0;i<n;i++)
            g[i]=g[i]%2;
        for(int i=0;i<n;i++)
        {
            if(g[i]==0)
                ans++;
            if(g[i]==1)
                one++;
        }
        ans+=(one/2+(one%2!=0));
    }
    else if(p==3)
    {
        int one=0,two=0;
        for(int i=0;i<n;i++)
            g[i]=g[i]%3;
        for(int i=0;i<n;i++)
        {
            if(g[i]==0)
                ans++;
            if(g[i]==1)
                one++;
            if(g[i]==2)
                two++;
        }
        if(one>=two)
        {
            ans+=two;
            one-=two;
            //one/=3;
            ans+=one/3+(one%3!=0);
        }
        else if(one<two)
        {
            ans+=one;
            two-=one;
            //two/=3;
            ans+=two/3+(two%3!=0);
        }
    }
    else
    {
        int one=0,two=0,three=0;
        for(int i=0;i<n;i++)
            g[i]=g[i]%4;
        for(int i=0;i<n;i++)
        {
            if(g[i]==0)
                ans++;
            if(g[i]==1)
                one++;
            if(g[i]==2)
                two++;
            if(g[i]==3)
                three++;
        }
        ans+=(two/2);
        two%=2;
        if(one>=three)
        {
            ans+=three;
            one-=three;
            if(two==0)
            {
                ans+=one/4+(one%4!=0);
            }
            else
            {
                if(one<=2)
                    ans++;
                else
                {
                    ans++;
                    one-=2;
                    ans+=one/4+(one%4!=0);
                }
            }
        }
        else
        {
            ans+=one;
            three-=one;
            if(two==0)
            {
                ans+=three/4+(three%4!=0);
            }
            else
            {
                if(three<=2)
                    ans++;
                else
                {
                    ans++;
                    three-=2;
                    ans+=three/4+(three%4!=0);
                }
            }
        }
        // int flag=1;
        // if(one>=two&&two>=three&&flag)
        // {
        //     ans+=three;
        //     one-=three;
        //     ans+=(two/2);
        //     two=two%2;
        //     if(two==0)
        //     {
        //         ans+=one/4+(one%4!=0);
        //     }
        //     else
        //     {
        //         if(one)
        //     }
        // }
    }

    printf("Case #%d: %d\n",t,ans);
}


int main()
{
    //fread;
    //fwrite;
    int tc;
    scanf("%d",&tc);
    //cout<<tc<<endl;
    for(int t=1;t<=tc;t++)
    {
        cin>>n>>p;
        for(int i=0;i<n;i++)
        {
            cin>>g[i];

        }
        solve(t);

    }
    return 0;
}
