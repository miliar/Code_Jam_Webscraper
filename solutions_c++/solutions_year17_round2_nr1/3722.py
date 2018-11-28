#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int,int> ii;
double f(ii a,int D) {
    int remain = D-a.first;
    double t = (double)remain / (double)a.second;
    return (double)D / t;
}
double f2(ii a,ii b) {
    return (b.first-a.first)/(a.second-b.second);
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        int D,N;
        scanf("%d%d",&D,&N);
        vector<ii> v;
        while ( N-- ) {
            int K,S;
            scanf("%d %d",&K,&S);
            v.push_back(ii(K,S));
        }
        sort(v.begin(),v.end());
        double ans = f(v[0],D);
        int idx = 0;
        for ( int i = 1 ; i < (int)v.size() ; i++ ) {
            if ( v[i].second >= v[idx].second ) continue;
            double t = f2(v[idx],v[i]);
            double pos = t*v[i].second + v[i].first;
            if ( pos > D ) continue;
            ans = f(v[i],D);
            idx = i;
        }
        printf("%.6lf\n",ans);
    }
    return 0;
}
