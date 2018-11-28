#include <bits/stdc++.h>

using namespace std;

#define vec vector
#define ALL(x) (x).begin(), (x).end()

typedef pair< int, int > pii;
typedef long long ll;

int const inf = 1000 * 1000 * 1000;
ll const inf64 = 1ll * inf * inf;

int const S = 50 * 1000 * 1000 + 5;

void solve() {
    int n, p;
    cin >> n >> p;
    vec< int > R(n);
    vec< vec< int > > Q(n, vec< int >(p));
    for(int i = 0;i < n;i++) {
        cin >> R[i];
    }
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < p;j++) {
            cin >> Q[i][j];
        }
    }
    vec< vec< pii > > seg(n);
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < p;j++) {
            int qR = 10 * Q[i][j] / (9 * R[i]);
            int qL = (10 * Q[i][j] + 11 * R[i] - 1) / (11 * R[i]);
//            cout << qL << " .. " << qR << "\n";
            if(qL <= qR) {
                seg[i].push_back(make_pair(qL, qR));
            }
        }
        sort(ALL(seg[i]));
    }
    vec< int > ptr(n);
    int res = 0;
    while(1) {
        int ql = -inf;
        int qr = +inf;
        int ok = 1;
        for(int i = 0;i < n;i++) {
            if(ptr[i] == (int)seg[i].size()) {
                ok = 0;
                break;
            }else {
                ql = max(ql, seg[i][ptr[i]].first);
                qr = min(qr, seg[i][ptr[i]].second);
            }
        }
        if(!ok) break;
        if(ql <= qr) {
            for(int i = 0;i < n;i++) {
                ptr[i]++;
            }
            res++;
        }else {
            int best = -1, L = inf;
            for(int i = 0;i < n;i++) {
                if(best == -1 || seg[i][ptr[i]].first < L) {
                    best = i;
                    L = seg[i][ptr[i]].first;
                }
            }
            ptr[best]++;
        }
    }
    cout << res << "\n";
}

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testNumber;

    scanf("%d", &testNumber);

    for(int test = 1;test <= testNumber;test++) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
