#include <iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
    freopen("data.out","w",stdout);
    int T;
    long long n,D;
    vector<pair<long long,long long> > G;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        G.clear();
        scanf("%lld%lld",&D,&n);
        for(int i=0;i<n;i++){
            long long a,b;
            scanf("%lld%lld",&a,&b);
            G.push_back(make_pair(a,b));
        }
        sort(G.begin(),G.end());
        pair<long long,long long> now;
        now=G[0];
        for(int i=0;i<G.size();i++){
            if(G[i].second*(D-now.first)<(now.second)*(D-G[i].first)) now=G[i];
        }
        double res=(1.0*D)/(1.0*(D-now.first)/now.second);
        printf("Case #%d: %.6lf\n",kase,res);
        /*
        if(kase==61){
            cout<<D<<" test "<<n<<endl;
            cout<<G[0].first<<" "<<G[0].second<<endl;
            printf("Case #%d: %.6lf\n",kase,res);
        }
        */
    }
    return 0;
}
