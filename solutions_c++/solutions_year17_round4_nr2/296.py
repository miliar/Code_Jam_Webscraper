#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define M 1010
int p[M], b[M], cp[M], cb[M];

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int n, c, m;
        scanf("%d%d%d", &n, &c, &m);
        memset(cp, 0, sizeof(cp));
        memset(cb, 0, sizeof(cb));
        for(int i=1; i<=m; i++){
            scanf("%d%d", p+i, b+i);
            cp[p[i]]++;
            cb[b[i]]++;
        }
        for(int i=2; i<=n; i++){
            cp[i] += cp[i-1];
        }
        int lb = 0;
        for(int i=1; i<=m; i++){
            lb = max(lb, cb[i]);
        }
        lb--;
        int ub = m;
        while(ub-lb > 1){
            int mid = (ub+lb)/2;
            bool ok = true;
            for(int i=1; i<=n; i++){
                if(cp[i] > mid*i){
                    ok=false; break;
                }
            }
            ok? ub=mid: lb=mid;
        }
        int ans2 = 0;
        for(int i=n, j=0; i>=1; i--){
            cp[i] -= cp[i-1];
            if(cp[i] >= ub){
                j += cp[i]-ub;
            }else{
                if(cp[i]+j <= ub){
                    ans2 += j;
                    j = 0;
                }else{
                    ans2 += ub-cp[i];
                    j -= ub-cp[i];
                }
            }
        }
        printf("Case #%d: %d %d\n", kase, ub, ans2);
    }
    return 0;
}
