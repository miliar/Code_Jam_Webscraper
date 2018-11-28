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

const int MAXN=200+3;
int A,B,N;
pair<pair<int,int>,bool> t[MAXN];
vector<int> space[2];

void init()
{
    N=A+B;
    for(int i=0;i<2;++i)
        space[i].clear();
}

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
        scanf("%d%d",&A,&B);
        init();
        int sum[2]={0};
        for(int i=0;i<A;++i)
        {
            scanf("%d%d",&t[i].fi.fi,&t[i].fi.se);
            sum[0]+=t[i].fi.se-t[i].fi.fi;
            t[i].se=0;
        }
        for(int i=A;i<N;++i)
        {
            scanf("%d%d",&t[i].fi.fi,&t[i].fi.se);
            sum[1]+=t[i].fi.se-t[i].fi.fi;
            t[i].se=1;
        }
        sort(t,t+N);
        int ans=0;
        for(int i=0;i<N;++i)
        {
            if(t[i].se!=t[(i+1)%N].se)
                ++ans;
            else
            {
//                cout<<"now: "<<i<<" next: "<<(i+1)%N<<endl;
                if(i==N-1)
                    space[t[i].se].push_back(t[(i+1)%N].fi.fi+24*60-t[i].fi.se);
                else space[t[i].se].push_back(t[(i+1%N)].fi.fi-t[i].fi.se);
//                cout<<"push: "<<space[t[i].se][space[t[i].se].size()-1]<<endl;
            }
        }
        sort(space[0].begin(),space[0].end());
        sort(space[1].begin(),space[1].end());
        int op;
        if(space[0].size()>0&&sum[0]+space[0][space[0].size()-1]>12*60)
            op=0;
        else op=1;
//        cout<<"size: "<<space[op].size()<<endl;
        if(space[op].size()>0)
            for(int i=space[op].size()-1;i>=0;--i)
            {
//                cout<<"sum: "<<sum[op]<<" space: "<<space[op][i]<<" add: "<<sum[op]+space[op][i]<<" obj: "<<12*60<<endl;
                if(sum[op]+space[op][i]>12*60)
                    ans+=2;
            }
        printf("Case #%d: %d\n",cas,ans);
    }
    
    return 0;
}
