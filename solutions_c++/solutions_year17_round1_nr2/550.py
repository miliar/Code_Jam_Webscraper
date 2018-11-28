#include <bits/stdc++.h>

using namespace std;

int T, C=1, n, p;
int q[64][64];
int r[64], atu[64];

void faixa(int ing, int v, int &a, int &b) {
    b = (v*10)/(9*r[ing]);
    a = (v*10 + 11*r[ing]-1)/(11*r[ing]);
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d",&n,&p);
        for (int i=0;i<n;i++)
            scanf("%d",r+i);
        for (int i=0;i<n;i++) {
            for (int j=0;j<p;j++)
                scanf("%d",&q[i][j]);
            sort(q[i],q[i]+p);
        }
        int resp = 0;
        for (int i=0;i<n;i++) atu[i]=0;
        int k=1;
        we:;
        while (1) {
            for (int i=0;i<n;i++) {
                int a, b;
                faixa(i,q[i][atu[i]],a,b);
                if (a <= k and k <= b) continue;
                if (b < k or a > b) {
                    atu[i]++;
                    if (atu[i]==p) goto fim;
                    goto we;
                }
                if (a > k) {
                    k = a;
                    goto we;
                }
            }
            resp++;
            for (int i=0;i<n;i++) {
                atu[i]++;
                if (atu[i]==p) goto fim;
            }
        }
        fim:;
        printf("%d\n",resp);
    }

    return 0;
}
