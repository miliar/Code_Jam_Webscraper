#include <cstdio>
using namespace std;
int d,n,k,s;
double ans,tans;
int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int tcas=1; tcas<=T; tcas++) {
        ans=-1.0;
        scanf("%d%d",&d,&n);
        for (int i=0; i<n; i++) {
            scanf("%d%d",&k,&s);
            tans=(double)d*s/(d-k);
            if (ans<0 || tans<ans) ans=tans;
        }
        printf("Case #%d: %.12f\n",tcas,ans);
    }
    return 0;
}
