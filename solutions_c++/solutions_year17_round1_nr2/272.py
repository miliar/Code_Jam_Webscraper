#include <bits/stdc++.h>
using namespace std;

const int N = 1024;

int n, p, r[N];

vector <int> s[N];
int it[N];

int check(int x, int y) {
    if (y * 10 < x * 9) return -1;
    if (y * 10 > x * 11) return 1;
    return 0;
}

int main() {
    int T, x;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++ i) {
            scanf("%d", &r[i]);
        }
        for (int i = 0; i < n; ++ i) {
            s[i].clear();
            for (int j = 0; j < p; ++ j) {
                scanf("%d", &x);
                s[i].push_back(x);
            }
            sort(s[i].begin(), s[i].end());
        }
        memset(it, 0, sizeof it);
        int i = 1;
        int tot = 0;
        while (true) {
            //printf("%d\n", i);
            int num0 = 0, num1 = 0, numf = 0;
            bool flag = true;
            for (int j = 0; j < n; ++ j) {
                while (it[j] < p && check(i * r[j], s[j][it[j]]) == -1) {
                    it[j] ++;
                }
                if (it[j] >= p) {
                    flag = false;
                    break;
                }
                int ck = check(i * r[j], s[j][it[j]]);
                if (ck == 0) {
                    num0 ++;
                } else if (ck == 1) {
                    num1 ++;
                }
            }
            if (num0 == n) {
                tot ++;
                for (int j = 0; j < n; ++ j) {
                    it[j] ++;
                    if (it[j] >= p) {
                        flag = false;
                        break;
                    }
                }
            } else {
                i ++;
            }
            if (!flag) break;
        }
        printf("Case #%d: %d\n", cas, tot);
    }
    return 0;
}
