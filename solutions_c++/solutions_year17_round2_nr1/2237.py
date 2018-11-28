#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;
pair<int,int> horses[1005];
bool cmpf(pair<int,int> a,pair<int,int> b){
    return a.first < b.first;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int d,n;
    for(int tc = 1; tc <= t; tc++){
        scanf("%d%d",&d,&n);
        for(int i = 0; i < n; i++){
            scanf("%d%d",&horses[i].first,&horses[i].second);
        }
        sort(horses,horses+n,cmpf);
        double mxt = 0.0;
        for(int i = 0; i < n; i++){
            mxt = max(mxt,(double)(d - horses[i].first)/horses[i].second);
        }
        printf("Case #%d: %.6f\n",tc,d/mxt);
    }
    return 0;
}
