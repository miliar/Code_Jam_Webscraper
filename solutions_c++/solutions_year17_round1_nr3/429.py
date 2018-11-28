#include <bits/stdc++.h>


using namespace std;
const int N = 66;
const int inf = (1 << 29);
int h1, h2, a1, a2, b, d;

// 减对方伤害， 加自己伤害
int gao(int x, int y) {
    int health1 = h1;
    int health2 = h2;
    int attack1 = a1;
    int attack2 = a2;
    int ret = 0;
    for(int i = 0, j = 0 ; i < x ; j ++) {
        if(i == 0 && j > 5) return inf;
        if(i && j > i * 4) return inf;
        ret ++;
        if(health1 <= max(0, attack2 - d)) {
            health1 = h1;
        }
        else {
            attack2 = max(0, attack2 - d);
            i ++;
        }

        health1 -= attack2;
        if(health1 <= 0) return inf;
    }
    for(int i = 0 , j = 0 ; i < y ; j ++) {
        if(i == 0 && j > 5) return inf;
        if(i && j > i * 4) return inf;
        ret ++;
        if(health1 <= attack2) {
            health1 = h1;
        }
        else {
            attack1 += b;
            i ++;
        }
        health1 -= attack2;
        if(health1 <= 0) return inf;
    }
    for(int i = 0 , j = 0 ;  ; j ++) {
        if(i == 0 && j > 5) return inf;
        if(i && j > i * 4) return inf;
        ret ++;
        if(health2 > attack1 && health1 <= attack2) {
            health1 = h1;
        }
        else {
            health2 -= attack1;
            i ++;
        }
        if(health2 <= 0) return ret;
        health1 -= attack2;
        if(health1 <= 0) return inf;
    }
    return inf;
}

int main () {

    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t --) {
        printf("Case #%d: ", ++ cas);
        scanf("%d %d %d %d %d %d", &h1, &a1, &h2, &a2, &b, &d);
        int ans = inf;
        for(int i = 0 ; i <= 100 ; i ++) {
            for(int j = 0 ; j <= 100 ; j ++) {
                ans = min(ans , gao(i, j));
            }
        }
        if(ans == inf) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }


    return 0;
}