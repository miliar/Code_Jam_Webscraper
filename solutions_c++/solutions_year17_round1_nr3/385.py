#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <iostream>
using namespace std;

int Hd, Ad, Hk, Ak, B, D;
const int maxn = 100 + 5;
const int inf = 0x3f3f3f3f;

struct Node {
    int hd, ad, hk, ak, act;
    Node(int hd = 0, int ad = 0, int hk = 0, int ak = 0, int act = 0):
        hd(hd),ad(ad), hk(hk), ak(ak), act(act) {}
};

int dp[maxn][maxn][maxn][maxn][2];

bool check(Node s) {
    return dp[s.hd][s.ad][s.hk][s.ak][s.act] == -1;
}

int solve() {
    memset(dp, -1, sizeof(dp));
    Node s(Hd, Ad, Hk, Ak, 0);
    dp[Hd][Ad][Hk][Ak][0] = 0;
    queue<Node> que;
    que.push(s);
    while(!que.empty()) {
        Node cur = que.front(); que.pop();
        int hd = cur.hd, ad = cur.ad, hk = cur.hk, ak = cur.ak;
        int act = cur.act;
        if (hk == 0) {
            return dp[hd][ad][hk][ak][act];
        }
        Node ns[4];
        int mx = 0;
        if (act == 0) {
            ns[0] = Node(hd, ad, max(0, hk - ad), ak, 1);
            ns[1] = Node(hd, min(ad + B, 100), hk, ak, 1);
            ns[2] = Node(Hd, ad, hk, ak, 1);
            ns[3] = Node(hd, ad, hk, max(0, ak - D), 1);
            mx = 4;
        } else {
            ns[0] = Node(max(0, hd - ak), ad, hk, ak, 0);
            mx = 1;
        }
        for (int i = 0; i < mx; i++) {
            if(check(ns[i])) {
                if(ns[i].hd == 0) continue;
                dp[ns[i].hd][ns[i].ad][ns[i].hk][ns[i].ak][ns[i].act] =
                    dp[hd][ad][hk][ak][act] + 1;
                que.push(ns[i]);
            }
        }
    }
    return -1;
}

int main() {
    int T; cin >> T;
    for (int Cas = 1; Cas <= T; Cas++) {
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
        int res = solve();
        printf("Case #%d: ", Cas);
        if (res == -1) puts("IMPOSSIBLE");
        else printf("%d\n", (res + 1) / 2);
    }
    return 0;
}
