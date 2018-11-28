#include<bits/stdc++.h>

using namespace std;

int T;
int a[105];
int c[5];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    int cs = 1;
    while(T--) {
        int N, P;
        scanf("%d%d",&N,&P);
        memset(c, 0, sizeof(c));
        for(int i = 1; i <= N; i++) {
            scanf("%d",&a[i]);
            c[a[i]%P]++;
        }
        int res = c[0];
        if(P == 2) {
            res += (c[1]+1) / 2;
        }
        else if(P == 3) {
            if(c[1] >= c[2]) {
                res += c[2];
                res += (c[1] - c[2] + 2) / 3;
            }
            else {
                res += c[1];
                res += (c[2] - c[1] + 2) / 3;
            }
        }
        else {

        }
        printf("Case #%d: %d\n",cs++,res);

    }

}
