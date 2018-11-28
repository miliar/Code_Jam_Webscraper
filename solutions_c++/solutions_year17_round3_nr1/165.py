#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <cmath>
using namespace std;
const double pi=atan(1.0)*4;
struct node
{
    long long r,h;
    node(){}
    node(int r,int h):r(r),h(h){}
    bool operator<(const node& rhs)
    {
        return r>rhs.r||(r==rhs.r&&h>rhs.h);
    }
};
vector<node> G;
int main()
{
    freopen("data.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        G.clear();
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++){
            int x,y;
            scanf("%d%d",&x,&y);
            G.push_back(node(x,y));
        }
        sort(G.begin(),G.end());
        long long res=0;
        for(int i=0;i<n;i++){
            if(n-i-1<k-1) break;
            long long tp=G[i].r*G[i].r+G[i].r*G[i].h*2;
            priority_queue<long long> Q;
            for(int j=i+1;j<n;j++){
                Q.push(G[j].r*G[j].h*2);
            }
            for(int j=0;j<k-1;j++){
                tp+=Q.top();Q.pop();
            }
            res=max(res,tp);
        }
        //cout<<res<<endl;
       // cout<<pi<<endl;
        double R=res*pi;
        //cout<<R<<endl;
        printf("Case #%d: %.9f\n",kase,R);
    }
    return 0;
}
