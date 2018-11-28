#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 1005;

int n, c, m, prom, count[maxn];
std::vector<std::pair<int,int>> t;

bool can(int S) {
    prom = 0;
    for (int i = 0; i < c; i++) count[i] = 0;
    int extra = 0;
    int i = 0;
    for (int curplace = 0; curplace < n; curplace++) {
        int thisrow = S;
        while (i < sz(t) && t[i].first == curplace) {
            int perplace, person; std::tie(perplace, person) = t[i];
            count[person]++;
            if (count[person] > S) return false;
            if (thisrow == 0) {
                if (extra == 0) return false;
                extra--;
                prom++;
            } else {
                thisrow--;
            }
            i++;
        }
        extra += thisrow;
    }
    return true;
}

int main() {
    int Testcases;
    scanf("%d", &Testcases);
    for (int testcase = 1; testcase <= Testcases; testcase++) {
        scanf("%d%d%d", &n, &c, &m);
        t.resize(m);
        for (int i = 0; i < m; i++) {
            scanf("%d%d", &t[i].first, &t[i].second);
            t[i].first--;
            t[i].second--;
        }
        std::sort(t.begin(), t.end());
        int lo = 1, hi = 1001, ans = 1001, ansprom;
        while (lo <= hi) {
            int mid = (lo+hi)/2;
            if (can(mid)) {
                hi = mid-1;
                ans = mid;
                ansprom = prom;
            } else {
                lo = mid + 1;
            }
        }
        printf("Case #%d: %d %d\n", testcase, ans, ansprom);
    }
}

