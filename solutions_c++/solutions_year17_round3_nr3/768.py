#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <ctime>
using namespace std;
#define INF 0x3f3f3f3f
#define LL long long
#define fi first
#define se second
#define mem(a,b) memset((a),(b),sizeof(a))
//#define TEST

const int MAXN=50+3;
const double eps=1e-7;
int N,K;
double U,p[MAXN];

int main()
{
#ifndef TEST
    freopen("/Users/xuehao/Documents/s1/in", "r", stdin);
    freopen("/Users/xuehao/Documents/s1/out", "w", stdout);
#endif
    int T_T;
    scanf("%d",&T_T);
    for(int cas=1;cas<=T_T;++cas)
    {
        scanf("%d%d%lf",&N,&K,&U);
        for(int i=0;i<N;++i)
            scanf("%lf",&p[i]);
        sort(p,p+N);
        double ans=0;
        for(int i=0;i<N;++i)
        {
            double sum=0,res=1;
            for(int j=0;j<=i;++j)
                sum+=p[j];
//            cout<<"sum0: "<<sum;
            sum+=U;
            double ave=sum/(i+1);
            ave=min(ave,1.0);
            if(ave<p[i])
                break;
//            cout<<" sum: "<<sum<<" ave: "<<ave<<endl;
            for(int j=0;j<=i;++j)
                res*=ave;
            for(int j=i+1;j<N;++j)
                res*=p[j];
            ans=max(ans,res);
        }
        printf("Case #%d: %.6f\n",cas,ans);
    }
    
    return 0;
}
