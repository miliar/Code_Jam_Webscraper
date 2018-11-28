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

int d,n;
int k[1010],s[1010];

int main()
{
//    fread;
//   fwrite;
    int tc;
    scanf("%d",&tc);
    int cs=1;
    while(tc--)
    {
        scanf("%d%d",&d,&n);
        double mx=0.0;
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&k[i],&s[i]);
            mx=max((double)(d-k[i])/s[i],mx);
        }

//        int l=d-k[n-1];
//        double t=(l*1.0)/(s[n-1]*1.0);
//        double tc;
//        double dc;
//        for(int i=n-2;i>=0;i--)
//        {
//            int len=d-k[i];
//            double ti=(len*1.0)/(s[i]*1.0);
//            if(ti-t>eps)
//            {
//                t=ti;
//                continue;
//            }
//            else
//            {
//                double dt=(1.0*(k[i+1]-k[i]))/(1.0*(s[i]-s[i+1]));
//
//            }
//        }
//
        double ans=d/mx;
        printf("Case #%d: %lf\n",cs++,ans);
    }
    return 0;
}
