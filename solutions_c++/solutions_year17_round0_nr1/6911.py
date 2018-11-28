/****** HAREE KRISHNA   ******/

/*
                     শুনেছি তোমার ভীষণ রাগ ??
                        সে কি  রাগ,নাকি
                     মগজ কোণে পচন ধরা
                        পুরনো কোডের বাগ ?
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long int lld;
typedef unsigned long long int llu;

#define sf scanf
#define pf printf
#define ff first
#define ss second
#define PI acos(-1.0)
#define sq(x) (x)*(x)
#define nn printf("\n")
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define TEST(i,t)       lld i,t;scanf("%lld",&t);for(i=1;i<=t;i++)

#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d %d",&x,&y)
#define sci3(x,y,z) scanf("%d %d %d",&x,&y,&z)

#define pfi(x) printf("%d\n",x)
#define pfi2(x,y) printf("%d %d\n",x,y)
#define pfi3(x,y,z) printf("%d %d %d\n",x,y,z)

#define FOR(i, b, n)    for(lld i=b; i<=n; i++)
#define FORR(i, n, b)   for(lld i=n; i>=b; i--)

#define scs(str) scanf("%s",str)

#define pfs(str) printf("%s\n",str)

#define pb push_back

/*

ASCII Vlaue
A=65,Z=90,a=97,z=122,0=48,9=57
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

*/
#define chk1 printf("chek1\n")
#define chk2 printf("chek2\n")
#define chk3 printf("chek3\n")
#define sz 2005
#define sz1 100005

/******   start your code   *******/

string st;
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    lld n,m,ap,am,c,d,x,y,k;
    TEST(tt,t)
    {
        cin>>st;
        sf("%lld",&k);
        n=st.size();
        m=0;
        c=0;
        FOR(i,0,n-1)
        {
            if(st[i]=='-')
            {
                x=y=0;
                if(n-i<k)
                {
                    FORR(j,n-1,n-k)
                    {
                        if(st[j]=='-')
                        {
                            st[j]='+';
                            x+=1;
                        }
                        else
                        {
                            st[j]='-';
                            y+=1;
                        }
                    }
                    if(y!=0)
                    {
                        c=1;
                        break;
                    }
                }
                else
                    FOR(j,i,i+k-1)
                {
                    if(st[j]=='-')
                        st[j]='+';
                    else
                        st[j]='-';
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



