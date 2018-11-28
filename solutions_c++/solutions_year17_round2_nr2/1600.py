#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        int a;
        scanf("%d", &a);
        int r, o, y, g, b, i, v;
        scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);
        vector<pair<int, char>> u;
        u.push_back({r, 'R'});
        u.push_back({y, 'Y'});
        u.push_back({b, 'B'});
        sort(u.begin(), u.end(), greater<pair<int, char>>());
        vector<char> res(u[0].first * 3, '?');
        for (int i = 0; i < u[0].first; i++) {
            res[i * 3] = u[0].second;
        }
        for (int i = 0; i < u[1].first; i++) {
            res[i * 3 + 1] = u[1].second;
        }
        for (int i = 0; i < u[2].first; i++) {
            res[res.size() - 1 - i * 3] = u[2].second;
        }
        vector<char> ou;
        for (int i = 0; i < res.size(); i++) {
            if (res[i] != '?') {
                ou.push_back(res[i]);
            }
        }
        bool poss = true;
        if (ou.front() == ou.back()) {
            poss = false;
        }
        for (int i = 0; i < ou.size() - 1; i++) {
            if (ou[i] == ou[i+1]) {
                poss = false;
            }
        }
        if (poss) {
            printf("Case #%d: ", c);
            for (char c : ou) {
                printf("%c", c);
            }
        } else {
            printf("Case #%d: IMPOSSIBLE", c);
        }
        printf("\n");
    }
    return 0;
}
