#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

const int MAXN = 1000;



int main() {
    freopen("control.in","r",stdin);
    freopen("control.out","w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
        int D, n;
        double tim = 0;
        scanf("%d%d",&D,&n);
        for (c=0;c<n;c++) {
            int pos ,v;
            scanf("%d%d",&pos,&v);
            tim = max(tim, (1. * D - pos) / v);
        }
        printf("Case #%d: %.8f\n",test, D / tim);
    }
    
    return 0;
}
