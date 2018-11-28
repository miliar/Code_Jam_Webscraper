#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>

using namespace std;


const int N = 110;
const int Q = 110;
const double MAX = 1e256;

int n;
int e[N], s[N];
int dst[N][N];
int sp[N][N];
double h[N][N];

double ans[Q];

void make_apsp() {
    for (int i=0; i<n; i++)
        for (int j=0; j<n; j++)
            sp[i][j] = dst[i][j];
    for (int k=0; k<n; k++)
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                if (sp[i][k]>0 && sp[k][j]>0)
                    if (sp[i][j]<0 || sp[i][j] > sp[i][k]+sp[k][j])
                        sp[i][j] = sp[i][k] + sp[k][j];
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++)
            if (sp[i][j] > 0 && sp[i][j]<=e[i]) {
                h[i][j] = sp[i][j]*1.0 / s[i];
            } else {
                h[i][j] = -1;
            }
    }
    /*
        puts("");
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                printf("%.2f ", h[i][j]);
            puts("");
        }
        */
    for (int k=0; k<n; k++)
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                if (h[i][k]>0 && h[k][j]>0)
                    if (h[i][j]<0 || h[i][j] > h[i][k]+h[k][j])
                        h[i][j] = h[i][k]+h[k][j];
}

double dp[N];

int main() {
    int t;
    int q, u, v;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        scanf("%d %d", &n, &q);
        for (int i=0; i<n; i++)
            scanf("%d %d", e+i, s+i);
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                scanf("%d", &dst[i][j]);

        make_apsp();

        /*
        puts("");
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                printf("%.2f ", h[i][j]);
            puts("");
        }
        puts("");
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                printf("%d ", sp[i][j]);
            puts("");
        }
        */

        for (int i=0; i<q; i++) {
            scanf("%d %d",  &u, &v);
            u--; v--;
            ans[i] = h[u][v];
        }

        printf("Case #%d:", o);
        for (int i=0; i<q; i++) 
            printf(" %f", ans[i]);
        puts("");
    }
}

