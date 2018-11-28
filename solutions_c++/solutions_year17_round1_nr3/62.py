#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <memory.h>
#include <iomanip>
#include <queue>

using namespace std;

const int N = 107;
const int INF = (int)2e9;

int f[N][N][N][N];

queue<int> qhd, qad, qhk, qak;

void solve() {
    int hd, ad, hk, ak, b, d;
    scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
    for (int i = 0; i <= 105; i++) {
        for (int j = 0; j <= 105; j++) {
            for (int u = 0; u <= 105; u++) {
                for (int k = 0; k <= 105; k++) {
                    f[i][j][u][k] = INF;
                }
            }
        }
    }
    while (!qhd.empty()) qhd.pop();
    while (!qad.empty()) qad.pop();
    while (!qhk.empty()) qhk.pop();
    while (!qak.empty()) qak.pop();
    qhd.push(hd);
    qad.push(ad);
    qhk.push(hk);
    qak.push(ak);
    f[hd][ad][hk][ak] = 0;
    int ans = INF;
    while (!qhd.empty()) {
        int my_health = qhd.front();
        int my_attack = qad.front();
        int his_health = qhk.front();
        int his_attack = qak.front();
        qhd.pop();
        qad.pop();
        qhk.pop();
        qak.pop();
        int value = f[my_health][my_attack][his_health][his_attack] + 1;
        if (my_attack >= his_health) {
            ans = min(ans, value);
        }
        if (my_attack <= his_health && my_health > his_attack && f[my_health - his_attack][my_attack][his_health - my_attack][his_attack] == INF) {
            f[my_health - his_attack][my_attack][his_health - my_attack][his_attack] = value;
            qhd.push(my_health - his_attack);
            qad.push(my_attack);
            qhk.push(his_health - my_attack);
            qak.push(his_attack);
        }
        int my_new_attack = min(101, my_attack + b);
        if (my_health > his_attack && f[my_health - his_attack][my_new_attack][his_health][his_attack] > value) {
            f[my_health - his_attack][my_new_attack][his_health][his_attack] = value;
            qhd.push(my_health - his_attack);
            qad.push(my_new_attack);
            qhk.push(his_health);
            qak.push(his_attack);
        }
        int my_new_health = hd;
        if (my_new_health > his_attack && f[my_new_health - his_attack][my_attack][his_health][his_attack] > value) {
            f[my_new_health - his_attack][my_attack][his_health][his_attack] = value;
            qhd.push(my_new_health - his_attack);
            qad.push(my_attack);
            qhk.push(his_health);
            qak.push(his_attack);
        }
        int his_new_attack = max(0, his_attack - d);
        if (my_health > his_new_attack && f[my_health - his_new_attack][my_attack][his_health][his_new_attack] > value) {
            f[my_health - his_new_attack][my_attack][his_health][his_new_attack] = value;
            qhd.push(my_health - his_new_attack);
            qad.push(my_attack);
            qhk.push(his_health);
            qak.push(his_new_attack);
        }
    }
    if (ans == INF) {
        puts("IMPOSSIBLE");
    } else {
        printf("%d\n", ans);
    }
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d", &tc);
    for (int i = 1; i <= tc; i++) {
        printf("Case #%d: ", i);
        solve();
        cerr << i << endl;
    }
    return 0;
}