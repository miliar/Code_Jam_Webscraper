//
// Created by Denis Mukhametianov on 08.04.17.
//

#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

const int maxn = 100;

int rec[maxn];
int q[maxn][maxn];
vector<int> v[maxn];
int minPossible[maxn][maxn];
int maxPossible[maxn][maxn];
int mt[maxn];
int used[maxn];
int timer = 100;


bool intersects(int a, int b, int c, int d) {
    return a <= b && c <= d && max(a, c) <= min(b, d);
}

bool kuhn(int e) {
    if(used[e] == timer)
        return false;
    used[e] = timer;
    for(int i = 0; i < v[e].size(); i++) {
        int to = v[e][i];
        if(mt[to] == -1 || kuhn(mt[to])) {
            mt[to] = e;
            return true;
        }
    }
    return false;
}

void solveB(int testNumber) {
    int n, p;
    cin >> n >> p;
    for (int i = 0; i < n; i++)
        cin >> rec[i];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            cin >> q[i][j];
            minPossible[i][j] = (10 * q[i][j]) / (11 * rec[i]) + ((10 * q[i][j]) % (11 * rec[i]) == 0 ? 0 : 1);
            maxPossible[i][j] = 10 * q[i][j] / (9 * rec[i]);
        }
    }
    int ans = 0;
    if (n == 1) {
        for (int i = 0; i < p; i++)
            if (minPossible[0][i] <= maxPossible[0][i])
                ans++;
    } else if (n == 2) {
        for (int i = 0; i < p; i++) {
            v[i].clear();
            for (int j = 0; j < p; j++)
                if (intersects(minPossible[0][i], maxPossible[0][i], minPossible[1][j], maxPossible[1][j]))
                    v[i].push_back(j);
        }
//        for(int i = 0; i < p; i++)
//        {
//            for(int j = 0; j < v[i].size(); j++)
//                printf("%d ", v[i][j]);
//            printf("\n");
//        }
//        printf("\n");
        memset(mt, -1, sizeof(mt));
        for (int i = 0; i < p; i++) {
            timer++;
            if (kuhn(i))
                ans++;
        }
    }
    printf("Case #%d: %d\n", testNumber, ans);
}

void runB() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++)
        solveB(i + 1);
}