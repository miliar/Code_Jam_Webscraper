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
#define TEST int test,zz;scanf("%d",&zz);getchar();for(test=1;test<=zz;test++)

#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d %d",&x,&y)
#define sci3(x,y,z) scanf("%d %d %d",&x,&y,&z)

#define pfi(x) printf("%d\n",x)
#define pfi2(x,y) printf("%d %d\n",x,y)
#define pfi3(x,y,z) printf("%d %d %d\n",x,y,z)

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

const int INF = 0x7f7f7f7f;

/******   start your code   *******/

double kim[1010],sped[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    lld num,n;
    int tot;
    double dis;
    sf("%d",&tot);
    for(int i=1; i<=tot; i++)
    {
        sf("%lf %lld",&dis,&n);
        double mn=0.000000;
        for(int k=0; k<n; k++)
        {
            sf("%lf %lf",&kim[k],&sped[k]);
            double temp=(dis-kim[k])/sped[k];
            if(temp>=mn) mn=temp;
        }
        pf("Case #%d: %0.6lf\n",i,dis/mn);
    }
    return 0;
}

/*
input:

output:

*/
