#include<bits/stdc++.h>
using namespace std;

char c[55][55];

int main() {

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {
        printf("Case #%d:\n", tt);

        int n,m,i,j,k,pi,pj;

        scanf("%d%d", &n, &m);
        for(i=0; i<n; i++) {
            scanf("%s", &c[i]);
            j=0;
            //prazan[i] = true;
            while(j<m) {
                pj = j;
                while(pj<m && c[i][pj] == '?') pj++;
                if (pj<m) {
                    //prazan[i] = false;
                    for(k=j; k<pj; k++) c[i][k] = c[i][pj];
                } else {
                    if (j > 0) {
                        for(k=j; k<pj; k++) c[i][k] = c[i][j-1];
                    }
                }
                j = pj+1;
            }
        }

        for(j=0; j<m; j++) {
            i = 0;
            while(i<n) {
                pi = i;
                while(pi<n && c[pi][j] == '?') pi++;

                if (pi < n) {
                    for(k=i; k<pi; k++) c[k][j] = c[pi][j];
                } else {
                    for(k=i; k<pi; k++) c[k][j] = c[i-1][j];
                }
                i = pi+1;
            }
        }

        for(i=0; i<n; i++) printf("%s\n", c[i]);
    }

    return 0;
}
