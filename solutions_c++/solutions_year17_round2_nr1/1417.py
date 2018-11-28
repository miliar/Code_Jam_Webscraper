#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int teesee, d, n, x, y;
    double latest;
    scanf("%d", &teesee);
    for(int asd=0; asd<teesee; asd++){
        latest = 0;
        scanf("%d%d", &d, &n);
        for(int i=0; i<n; i++){
            scanf("%d%d", &x, &y);
            latest = max(latest, ((double)(d-x))/y);
        }
        printf("Case #%d: %.6f\n", asd+1, ((double)d)/latest);
    }
}
