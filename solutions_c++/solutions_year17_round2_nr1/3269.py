/* ***********************************************
 Author        :shuaibaobao
 Created Time  :
 File Name     :
 ************************************************ */

#include <iostream>
#include <map>

using namespace std;

const int maxn = 1010;
const int inf = 0x3f3f3f3f;
int t;
pair<long long,int>num[maxn];

int main(){
    scanf("%d",&t);
    int cas = 1;
    while(t--){
        long long dist;
        int n;
        scanf("%lld%d",&dist,&n);
        for(int i = 1;i <= n;++ i){
            scanf("%lld%d",&num[i].first,&num[i].second);
        }
        double t = 0;
        for(int i = 1;i <= n;++ i){
            double ans = 1.0*(dist-num[i].first)/num[i].second;
            t = max(ans,t);
        }
        printf("Case #%d: ",cas);
        cas++;
        printf("%.6lf\n",dist/t);
    }
    return 0;
}
