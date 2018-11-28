#include<bits/stdc++.h>
using namespace std;

#define MAXBR 1000111

struct qqq {
    int mink,maxk;
} q[55][55];

bool cmp(qqq a, qqq b) {
    return a.mink < b. mink || (a.mink == b.mink && a.maxk < b.maxk);
}

int r[55],pok[55],cnt[55][MAXBR];

bool moze(int x, int y) {
    return (9*x <= 10*y && 10*y <= 11*x);
}

void init(int n) {
    int i,j;
    for(i=0; i<n; i++) {
        for(j=0; j<=MAXBR; j++) {
            cnt[i][j] = 0;
        }
    }
}

int main() {

    int n,p,i,j,t,qq,br,mc,mbr,res,mind,mink,maxk;

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {
        printf("Case #%d: ", tt);

        scanf("%d%d", &n, &p);

        init(n);

        for(i=0; i<n; i++) {
            scanf("%d", &r[i]);
        }

        for(i=0; i<n; i++) {
            for(j=0; j<p; j++) {
                scanf("%d", &qq);
                q[i][j].maxk = (10*qq) / (9*r[i]);
                q[i][j].mink = (10*qq) / (11*r[i]) + (((10*qq) % (11*r[i])) > 0);
            }
            sort(q[i], q[i]+p, cmp);
            pok[i] = 0;
        }

        res = 0;
        while(true) {

            mind = 0;

            mink = q[0][pok[0]].mink;
            maxk = q[0][pok[0]].maxk;

            for(i=1; i<n; i++) {
                mink = max(mink, q[i][pok[i]].mink);
                maxk = min(maxk, q[i][pok[i]].maxk);

                if (cmp(q[i][pok[i]], q[mind][pok[mind]])) {
                    mind = i;
                }
            }

            if (mink <= maxk) {
                res++;
                bool bb = false;
                for(i=0; i<n; i++) {
                    pok[i]++;
                    if (pok[i] >= p) bb = true;
                }
                if (bb) break;
            } else {
                pok[mind]++;
                if (pok[mind] >= p) break;
            }
        }

        printf("%d\n", res);
//
//        mbr = 0;
//        for(i=0; i<n; i++) {
//            for(j=0; j<p; j++) {
//                scanf("%d", &q);
//                t = q/r[i];
//                if (moze(t*r[i], q)) br = t;
//                else if (moze((t+1)*r[i], q)) br = t+1;
//                else br = -1;
//
//                if (br!=-1) {
//                    cnt[i][br]++;
//                }
//
//                printf("-> %d %d -> %d\n", i, j, br);
//
//                mbr = max(mbr, br);
//            }
//        }
//
//        res = 0;
//        for(br=1; br<=mbr; br++) {
//            mc = cnt[0][br];
//            for(i=1; i<n; i++) mc = min(mc, cnt[i][br]);
//            res += mc;
//        }
//
//        printf("%d\n", res);
    }

    return 0;
}
