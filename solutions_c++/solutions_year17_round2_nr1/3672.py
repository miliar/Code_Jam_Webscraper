
#include <iostream>
#include <map>
#define maxm 101

using namespace std;
pair<long long,int>num[maxn];
int main()
{
    int T;
    long long dist;
    int n;
    double t;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%lld%d",&dist,&n);
        for(int i = 1;i <= n;++ i){
            scanf("%lld%d",&num[i].first,&num[i].second);
        }
        t = 0;
        for(int i = 1;i <= n;i++){
            double ans = 1.0*(dist-num[i].first)/num[i].second;
            t = max(ans,t);
        }
        printf("Case #%d: %.6lf\n",cas,dist/t);
    }
    return 0;
}
