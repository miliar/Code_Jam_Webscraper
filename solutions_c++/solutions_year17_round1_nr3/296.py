#include<bits/stdc++.h>
using namespace std;

struct igra {
    int hd,ad,hk,ak,p;
    igra(){}
    igra(int _hd, int _ad, int _hk, int _ak, int _p) {
        hd=_hd; ad=_ad; hk=_hk; ak=_ak; p=_p;
    }
};

queue<igra> que;
bool mark[111][111][111][111];

void init() {
    while(!que.empty()) que.pop();

    int i,j,k,l;

    for(i=0; i<=101; i++) {
        for(j=0; j<=101; j++) {
            for(k=0; k<=101; k++) {
                for(l=0; l<=101; l++) {
                    mark[i][j][k][l] = false;
                }
            }
        }
    }
}

void ubaci(int hd, int ad, int hk, int ak, int p) {
    if (!mark[hd][ad][hk][ak]) {
        que.push(igra(hd,ad,hk,ak,p));
        mark[hd][ad][hk][ak] = true;
    }
}

int main() {

    int HD,AD,HK,AK,B,D,res;
    igra tr;

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {
        printf("Case #%d: ", tt);

        scanf("%d%d%d%d%d%d", &HD, &AD, &HK, &AK, &B, &D);

        init();

        ubaci(HD,AD,HK,AK,0);

        res = -1;
        while(!que.empty()) {

            tr = que.front();
            que.pop();

            if (tr.hk == 0) {
                res = tr.p;
                break;
            }

            //attack
            if (tr.hk-tr.ad <= 0 || tr.hd > tr.ak) {
                ubaci(tr.hd-(tr.hk-tr.ad > 0)*tr.ak, tr.ad, max(0,tr.hk-tr.ad), tr.ak, tr.p+1);
            }

            //buff
            if (tr.hd > tr.ak) {
                ubaci(tr.hd-tr.ak, min(tr.ad+B,100), tr.hk, tr.ak, tr.p+1);
            }

            //cure
            if (HD > tr.ak) {
                ubaci(HD-tr.ak, tr.ad, tr.hk, tr.ak, tr.p+1);
            }

            //debuff
            if (tr.hd > max(0,tr.ak-D)) {
                ubaci(tr.hd-max(0,tr.ak-D), tr.ad, tr.hk, max(0,tr.ak-D), tr.p+1);
            }
        }

        if (res == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", res);
        }

    }

    return 0;
}
