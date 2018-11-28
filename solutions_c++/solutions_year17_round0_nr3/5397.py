#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define xx first
#define yy second

#ifndef _WIN32
#define gc getchar_unlocked
#else
#define gc getchar
#endif // _WIN32
void ri(int &a) {
    a = 0;
    register int x = gc();
    bool neg = false;
    while (x < '0' || x > '9') {
        if (x == '-') neg = true;
        x = gc();
    }
    while (x >= '0' && x <= '9') {
        a = (a << 3) + (a << 1) + (x-'0');
        x = gc();
    }
    if (neg) a = -a;
}

const int maxn = 1010, INF = (1 << 30)-1;

int t;

int main() {
    freopen("output.out", "w", stdout);
    cin >> t;
    for (int cs = 1, n, k; cs <= t; cs++) {
        printf("Case #%d: ", cs);
        cin >> n >> k;
        n += 2;
        set<int> locs;
        locs.insert(0);
        locs.insert(n-1);
        for (int i = 0; i < k; i++) {
            int ls = -1, rs = -1, nloc = -1;
            for(auto itr = locs.begin(); ; itr++) {
                auto nxt = itr;
                nxt++;
                if (nxt == locs.end()) break;
                int lft = *itr, rt = *nxt;
                int d = rt-lft-1;
                int cl = (d-1)/2, cr = d/2;
                if (min(cl, cr) > min(ls, rs)) {
                    ls = cl;
                    rs = cr;
                    nloc = (lft+rt)/2;
                } else if (min(cl, cr) == min(ls, rs)) {
                    if (max(cl, cr) > max(ls, rs)) {
                        ls = cl;
                        rs = cr;
                        nloc = (lft+rt)/2;
                    }
                }
            }
            if (i == k-1) {
                printf("%d %d\n", max(ls, rs), min(ls, rs));
            } else {
                locs.insert(nloc);
            }
        }
    }
    return 0;
}
