#include <bits/stdc++.h>

using namespace std;

int n, p;
int a[55];
int b[55][55];
int ip[55];


int fabs(int x, int y) {
    if(10 * x < 9 * y) return -1;
    else if(10 * x > 11 * y) return 1;
    return 0;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase ++) {
        scanf("%d%d", &n, &p);
        for(int i = 0; i < n; i ++) scanf("%d", &a[i]);
        for(int i = 0; i < n; i ++) {
            for(int j = 0; j < p; j ++) {
                scanf("%d", &b[i][j]);
            }
            sort(b[i], b[i] + p);
        }

        int ans = 0;
        int tm = 1;
        memset(ip, 0, sizeof(ip));
        while(true) {
            vector<int> xiaoyu;
            bool ok = false;
            for(int i = 0; i < n; i ++) {
                int jg = fabs(b[i][ip[i]], a[i] * tm);
                if(jg < 0) xiaoyu.push_back(i);
                else if(jg > 0) ok = true;
            }

            if(ok == false && xiaoyu.size() == 0) {
                ans ++;
                bool finish = false;
                for(int i = 0; i < n; i ++) {
                    ip[i] ++;
                    if(ip[i] >= p) finish = true;
                }
                if(finish) break;
            } else if(ok == false) {
                bool finish = false;
                for(int i = 0; i < xiaoyu.size(); i ++) {
                    ip[xiaoyu[i]] ++;
                    if(ip[xiaoyu[i]] >= p) finish = true;
                }
                if(finish) break;
            } else {
                tm ++;
            }
        }
        printf("Case #%d: %d\n", kase, ans);

    }
    return 0;
}
