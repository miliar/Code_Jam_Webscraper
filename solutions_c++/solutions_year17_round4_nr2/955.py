#include <cstdio>
#include <vector>
#include <algorithm>
int n, c, m;

using namespace std;

vector<vector<int> > ticket;

int Try_put(int t) {
    if (t <= 0) return -1;
    vector<vector<bool> > vst(t, vector<bool>(c, false));
    vector<int> cnt(t, 0);
    int promo = 0;
    int limit = t;
    for (int i = 0; i < n; i++) {
        vector<int> cur(t, 1);
        for (int j = 0, k = 0; j < ticket[i].size(); j++) {
            int times = 0;
            for (times = 0; times < limit; times++, k = (k + 1) % t) {
                if (cur[k] > 0 && !vst[k][ticket[i][j]]) {
                    vst[k][ticket[i][j]] = true;
                    cur[k]--;
                    break;
                }
            }
            if (times < limit) continue;
            for (times = 0; times < limit; times++, k = (k + 1) % t) {
                if (cnt[k] > 0 && !vst[k][ticket[i][j]]) {
                    vst[k][ticket[i][j]] = true;
                    cnt[k]--;
                    promo++;
                    break;
                }
            }
            if (times < limit) continue;
            return -1;
        }
        for (int l = 0; l < t; l++) cnt[l] += cur[l];
    }
    return promo;
}

int Try_put2(int t) {
    if (t <= 0) return -1;
    vector<vector<bool> > vst(t, vector<bool>(c, false));
    vector<int> cnt(t, 0);
    int promo = 0;
    int limit = t;
    for (int i = 0,  k = 0; i < n; i++) {
        vector<int> cur(t, 1);
        for (int j = 0; j < ticket[i].size(); j++) {
            int times = 0;
            for (times = 0; times < limit; times++, k = (k + 1) % t) {
                if (cur[k] > 0 && !vst[k][ticket[i][j]]) {
                    vst[k][ticket[i][j]] = true;
                    cur[k]--;
                    break;
                }
            }
            if (times < limit) continue;
            for (times = 0; times < limit; times++, k = (k + 1) % t) {
                if (cnt[k] > 0 && !vst[k][ticket[i][j]]) {
                    vst[k][ticket[i][j]] = true;
                    cnt[k]--;
                    promo++;
                    break;
                }
            }
            if (times < limit) continue;
            return -1;
        }
        for (int l = 0; l < t; l++) cnt[l] += cur[l];
    }
    return promo;
}

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d%d", &n, &c, &m);
        ticket.assign(n, vector<int>());
        for (int i = 0; i < m; i++) {
            int pi, bi;
            scanf("%d%d", &pi, &bi);
            pi--;bi--;
            ticket[pi].push_back(bi);
        }
        for (int i = 0; i < n; i++) sort(ticket[i].begin(), ticket[i].end());
        //Try_put(2);
        int l = 1, r = m;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (Try_put(mid) >= 0) r = mid - 1;
            else l = mid + 1;
        }
        printf("Case #%d: %d %d\n", cas, l, Try_put(l));
    }
    return 0;
}
/*
20
3 2 8
2 1
2 1
2 1
2 1
2 2
2 2
2 2
2 2
3 2 9
2 1
2 1
2 1
2 1
2 2
2 2
2 2
2 2
1 1

2 2 1
3 1
3 2 8
1 1
1 1
2 1
2 1
1 2
1 2
2 2
2 2
3 2 8
3 1
3 1
3 1
3 2
3 2
3 2
1 1
2 2
3 2 6
3 1
3 1
2 2
2 2
1 1
2 2
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1
3 2 9
1 1
1 1
1 2
2 2
2 2
2 1
3 1
3 2
3 1

*/
