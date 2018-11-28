#include <bits/stdc++.h>
using namespace std;

const int N = 256;
const int M = 128;

bool vis[M][N][M][N];

struct node {
    int hd, ad, hk, ak, stp;
    node(int _hd = 0, int _ad = 0, int _hk = 0, int _ak = 0, int _stp = 0) {
        hd = _hd;
        ad = _ad;
        hk = _hk;
        ak = _ak;
        stp = _stp;
    }
};

queue <node> q;
void print(node v) {
    printf("%d %d %d %d %d\n", v.hd, v.ad, v.hk, v.ak, v.stp);
}
int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        while (!q.empty()) q.pop();
        int hd, ad, hk, ak, b, d;
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        q.push(node(hd, ad, hk, ak, 0));
        vis[hd][ad][hk][ak] = true;
        memset(vis, 0, sizeof vis);
        int ans = -1;
        while (!q.empty()) {
            node u = q.front();
            q.pop();
            //print(u);
            node v;
            // attack
            v = u;
            v.stp ++;
            v.hk -= v.ad;
            //printf("----\n");
            //print(v);
            if (v.hk <= 0) {
                ans = v.stp;
                break;
            }
            v.hd -= v.ak;
            if (v.hd > 0 && !vis[v.hd][v.ad][v.hk][v.ak]) {
                vis[v.hd][v.ad][v.hk][v.ak] = true;
                q.push(v);
            }
            // buff
            v = u;
            v.stp ++;
            v.ad += b;
            v.hd -= v.ak;
            if (v.hd > 0 && !vis[v.hd][v.ad][v.hk][v.ak]) {
                vis[v.hd][v.ad][v.hk][v.ak] = true;
                q.push(v);
                //print(v);
            }
            // cure
            v = u;
            v.stp ++;
            v.hd = hd;
            v.hd -= v.ak;
            if (v.hd > 0 && !vis[v.hd][v.ad][v.hk][v.ak]) {
                vis[v.hd][v.ad][v.hk][v.ak] = true;
                q.push(v);
            }
            //debuff
            v = u;
            v.stp ++;
            v.ak -= d;
            v.ak = max(0, v.ak);
            v.hd -= v.ak;
            if (v.hd > 0 && !vis[v.hd][v.ad][v.hk][v.ak]) {
                vis[v.hd][v.ad][v.hk][v.ak] = true;
                q.push(v);
            }
        }
        printf("Case #%d: ", cas);
        if (ans == -1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
