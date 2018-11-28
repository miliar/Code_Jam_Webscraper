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

const int MAXN=1000+3;
const double PI=acos(-1.0);
int N,K;
pair<double,double> pan[MAXN];//raido,high
priority_queue<double> que;


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
        scanf("%d%d",&N,&K);
//        cout<<"N: "<<N<<" K: "<<K<<endl;
        for(int i=0;i<N;++i)
        {
            scanf("%lf%lf",&pan[i].fi,&pan[i].se);
        }
        sort(pan,pan+N);
        double ans=0;
        for(int i=K-1;i<N;++i)
        {
            double res=PI*pan[i].fi*pan[i].fi+2*PI*pan[i].fi*pan[i].se;
//            cout<<"i: "<<i<<" ans: "<<ans<<" fi: "<<pan[i].fi<<" se: "<<pan[i].se<<" res: "<<res<<endl;
            while(!que.empty())
                que.pop();
            for(int j=0;j<i;++j)
                que.push(2*PI*pan[j].fi*pan[j].se);
            for(int j=0;j<K-1;++j)
            {
//                cout<<"top: "<<que.top()<<" res: "<<res<<endl;
                res+=que.top(); que.pop();
            }
            ans=max(ans,res);
        }
        printf("Case #%d: %.9f\n",cas,ans);
    }
    
    return 0;
}
