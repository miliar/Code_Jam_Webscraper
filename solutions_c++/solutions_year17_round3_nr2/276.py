#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 220;

struct node {
    int l, r, type;
}a[N];

bool operator<(node x, node y) {
    return x.l < y.l;
}


int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        int n, m;
        scanf("%d%d", &n, &m);
        int ans = n;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int l, r;
            scanf("%d%d", &l, &r);
            a[i] = (node){l, r, 0}; 
            cnt += r - l;
        }
        for (int i = 0; i < m; i++) {
            int l, r;
            scanf("%d%d", &l, &r);
            a[i + n] = (node){l, r, 1}; 
        }
        n += m;
        sort(a, a + n);
        a[n] = a[0];
        a[n].l += 1440;
        vector<pair<int, int> > v;
        for (int i = 0; i < n; i++) {
            if (a[i].type == a[i + 1].type) {
                if (a[i].type == 0) v.emplace_back(0, a[i + 1].l - a[i].r);
                else v.emplace_back(2, -(a[i + 1].l - a[i].r));
            }
            else v.emplace_back(1, a[i + 1].l - a[i].r);
        }
        sort(v.begin(), v.end());
        cnt = 720 - cnt;
        for (auto it : v) {
            if (it.first == 0) {
                if (it.second <= cnt) ans--, cnt-=it.second;
                else break;
            }
            else if (it.first == 1) {
                cnt -= it.second;
                if (cnt <= 0) break;
            }
            else {
                if (cnt <= 0) break;
                ans++;
                cnt -= -it.second;
                if (cnt <= 0) break;
            }
        }
        printf("Case #%d: %d\n", _, ans*2);
    }
    return 0;
}
