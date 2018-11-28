/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/04/15
 *  Name:
 *      c.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int cas, hd, ad, hk, ak, b, d, hp;
struct node{
    int data;
    node() { }
    node(int hd, int ad, int hk, int ak) {
        data = (hd << 21) | (ad << 14) | (hk << 7) | ak;
    }

};
int dp[101][101][101][101];
queue<node> q;
int work() {
    while (!q.empty())
        q.pop();
    q.push(node(hd, ad, hk, ak));
    memset(dp, -1, sizeof dp);
    dp[hd][ad][hk][ak] = 0;
    while (!q.empty()) {
        int x = q.front().data;
        q.pop();
        int hd = x >> 21, ad = (x >> 14) & 127,
            hk = (x >> 7) & 127, ak = x & 127, nhd, nad, nhk, nak;
        int step = dp[hd][ad][hk][ak];
        //  attack
        nhd = hd, nad = ad, nhk = hk, nak = ak;
        nhk -= ad;
        nhd -= nak;
        if (nhk <= 0)
            return step + 1;
        if (nhd > 0 && dp[nhd][nad][nhk][nak] == -1) {
            dp[nhd][nad][nhk][nak] = step + 1;
            q.push(node(nhd, nad, nhk, nak));
        }

        //  buff
        nhd = hd, nad = ad, nhk = hk, nak = ak;
        nad += b;
        nhd -= nak;
        if (nhd > 0 && dp[nhd][nad][nhk][nak] == -1) {
            dp[nhd][nad][nhk][nak] = step + 1;
            q.push(node(nhd, nad, nhk, nak));
        }

        //  Cure
        nhd = hd, nad = ad, nhk = hk, nak = ak;
        nhd = hp;
        nhd -= nak;
        if (nhd > 0 && dp[nhd][nad][nhk][nak] == -1) {
            dp[nhd][nad][nhk][nak] = step + 1;
            q.push(node(nhd, nad, nhk, nak));
        }
        
        //  debuff
        nhd = hd, nad = ad, nhk = hk, nak = ak;
        nak = max(0, nak - d);
        nhd -= nak;
        if (nhd > 0 && dp[nhd][nad][nhk][nak] == -1) {
            dp[nhd][nad][nhk][nak] = step + 1;
            q.push(node(nhd, nad, nhk, nak));
        }
    }
    return -1;
}
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        hp = hd;
        int ans = work();
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, ans);
        }
    }

    

    return 0;
}
