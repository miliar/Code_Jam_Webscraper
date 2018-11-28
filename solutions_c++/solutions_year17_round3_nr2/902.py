#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int N = 1000;

struct PCK {
    int s;
    int e;
    int w;
};

int comp(PCK& __a, PCK &b) {
    return __a.s<b.s;
}
int comp2(int a, int b) {
    return a>b;
}
int sum(int *ary, int n) {
    int s = 0;
    for( int i=0; i<n; i++)
        s += ary[i];
    return s;
}


int main() {
    PCK as[N];
    int ass[2][N];
    int seg[2][2][N];
    int ns[2][2];
    int t;
    int cnt = 0;
    int tmp;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        int nj, nc;
        int an[2];
        int n;
        int nw;
        int ok;
        scanf("%d %d", &nj, &nc);
        an[0] = nj;
        an[1] = nc;
        n = nj+nc;
        cnt = 0;
        for (int i=0; i<nj; i++) {
            scanf("%d %d",  &as[i].s, &as[i].e);
            ass[0][i] = as[i].e-as[i].s;
            as[i].w = 0;
        }
        for (int i=nj; i<nj+nc; i++) {
            scanf("%d %d",  &as[i].s, &as[i].e);
            ass[1][i-nj] = as[i].e-as[i].s;
            as[i].w = 1;
        }
        sort(as, as+n, comp);
        as[n] = as[0];
        as[n].s += 1440;
        as[n].e += 1440;

        ns[0][0]=ns[0][1]=ns[1][0]=ns[1][1] = 0;

        for (int i=0; i<n; i++) {
            if (as[i].w != as[i+1].w)
                cnt += 1;
            int w1, w2;
            w1 = as[i].w; w2 = as[i+1].w;
            seg[w1][w2][ns[w1][w2]++] = as[i+1].s-as[i].e;
            //printf("seg...%d %d\n", as[i+1].s, as[i].e);
        }
        for (int i=0; i<2; i++)
            for (int j=0; j<2; j++) {
                sort(seg[i][j], seg[i][j]+ns[i][j], comp2);
            //    for (int l=0; l<ns[i][j]; l++)
            //       printf("%d ", seg[i][j][l]);
            //    puts("");
            }
        ok = 0;
        for (int i=0; i<=1&&!ok; i++) {
            //printf("%d %d\n",sum(ass[i], an[i]), sum(seg[i][i], ns[i][i]) );
            if ( sum(ass[i], an[i])+sum(seg[i][i], ns[i][i]) > 720) {
                //printf("here %d\n", i);
                int k = 1-i;
                nw = 720 - sum(ass[k], an[k]) - sum(seg[k][k], ns[k][k]);
                for (int l=0; l<ns[i][i]; l++) {
                    //printf("borrow: %d\n", seg[i][i][l]);
                    nw -= seg[i][i][l];
                    cnt += 2;
                    if (nw<=0) {
                        ok = 1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", o, cnt);
    }
}
