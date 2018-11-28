#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

class Area{
public:
    int st, ed, wh; // wh = 0 (A must), who = 1 (B must)
    Area() {}
    Area(int _s, int _e, int _w): st(_s), ed(_e), wh(_w) {}
};

int AA[105], AAcnt, AAtot;
int BB[105], BBcnt, BBtot;

bool cmp(Area a1, Area a2) {
    return a1.st < a2.st;
}

Area area[205];

int A, B, AB;

void solve() {
    int a, b, ans = 0;

    scanf("%d%d",&A,&B);
    AB = A+B;
    AAcnt = BBcnt = 0;
    AAtot = BBtot = 720;

    for (int i = 0; i < A; ++i) {
        scanf("%d%d",&a,&b);
        area[i] = Area(a,b,1);
    }
    for (int i = A; i < A+B; ++i) {
        scanf("%d%d",&a,&b);
        area[i] = Area(a,b,0);
    }

    if(AB == 1) {
        printf("2\n");
        return ;
    }

    sort(area,area+AB,cmp);
    area[AB] = Area(area[0].st+1440,area[0].ed+1440,area[0].wh);

    int tmp;
    for (int i = 0; i < AB; ++i) {

        tmp = area[i].ed-area[i].st;

        if (area[i].wh == 0)
            AAtot = AAtot - tmp;
        else
            BBtot = BBtot - tmp;

        tmp = area[i+1].st-area[i].ed;
        //printf("%d,%d,tmp = %d\n",area[i+1].st,area[i].ed,tmp);

        if (area[i].wh != area[(i+1)%AB].wh) { // not the same
            ++ans;
        }
        else { // curw == area[i].wh
            if (area[i].wh == 0) {// A must
                AA[AAcnt++] = tmp;
            }
            else { // == 1
                BB[BBcnt++] = tmp;
            }
        }
    }

    sort(AA,AA+AAcnt);
    for (int i = 0; i < AAcnt; ++i) {
        if (AAtot >= AA[i]) {
            AAtot -= AA[i];
        }
        else {
            ans = ans + (AAcnt-i)*2;
            break;
        }
    }

    sort(BB,BB+BBcnt);
    //printf("BBcnt=%d\n",BBcnt);
    for (int i = 0; i < BBcnt; ++i) {
        if (BBtot >= BB[i]) {
            BBtot -= BB[i];
        }
        else {
            ans = ans + (BBcnt-i)*2;
            break;
        }
    }

    printf("%d\n",ans);
}


int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
