#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int d,n;
int main(){
//    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d",&d,&n);
        double ans=1e16;
        for(int i=0;i<n;++i){
            int a,b;
            scanf("%d%d",&a,&b);
            ans=min(ans,(double)d*b/(d-a));
        }
        printf("Case #%d: ",ca);
        printf("%.6f\n",ans);
    }
    return 0;
}
