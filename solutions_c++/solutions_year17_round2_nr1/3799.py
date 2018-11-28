#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<string>
using namespace std;
typedef long long ll;
const int INF=0x3f3f3f3f;
double d;
int k;
double pos[1010],s[1010];

int check(double ss)
{
    double t=d/ss;
    for(int i=0;i<k;i++)
    {
        if(d>pos[i]+t*s[i])
            return 0;
    }
    return 1;
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int ca=1;
    while(t--)
    {
        scanf("%lf%d",&d,&k);
        for(int i=0;i<k;i++)
        {
            scanf("%lf%lf",&pos[i],&s[i]);
        }
        double l=0,r=1e16;
        for(int i=0;i<100;i++)
        {
            double m=(l+r)/2;
            if(check(m))
                l=m;
            else
                r=m;
        }
        printf("Case #%d: %.6lf\n",ca++,r);
    }
    return 0;
}
