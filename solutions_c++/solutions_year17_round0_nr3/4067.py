// written at 17:11 on 8 Apr 2017
#include <bits/stdc++.h>

#define IOS std::ios::sync_with_stdio(false); std::cin.tie(nullptr); std::cout.tie(nullptr);
// #define __DEBUG__
#ifdef __DEBUG__
#define DEBUG(...) printf(__VA_ARGS__)
#else
#define DEBUG(...)
#endif
#define filename "C-small-2-attempt1"
// #define filename "C-large"
#define setfile() freopen(filename".in.txt", "r", stdin); freopen(filename".ans.txt", "w", stdout);
#define resetfile() freopen("/dev/tty", "r", stdin); freopen("/dev/tty", "w", stdout); system("more " filename".ans.txt");
#define rep(i, j, k) for (int i = j; i < k; ++i)
#define irep(i, j, k) for (int i = j - 1; i >= k; --i)

using namespace std;

template <typename T>
inline T sqr(T a) { return a * a;};

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int > Pii;

const double pi = acos(-1.0);
const int INF = INT_MAX;
const ll LLINF = LLONG_MAX;
const int MAX_N = 1e5 + 10;

// struct Tri {
//     ll len, l, r;
//     Tri(int _len = 0, int _l = 0, int _r = 0) : len(_len), l(_l), r(_r) {};
//     bool operator < (const Tri &b) const {
//         int an = len - 1, bn = b.len - 1;
//         if (an / 2 != bn / 2) return an / 2 > bn / 2;
//         if (an / 2 + an % 2 != bn / 2 + bn % 2) return an / 2 + an % 2 > bn / 2 + bn % 2;
//         return l < b.l;
//     }
// };

int t, n, k, a1, a2;

int main() {
    setfile();
    scanf("%d", &t);
    for (int _ = 0; _ < t; _++) {
        scanf("%d%d", &n, &k);
        priority_queue<int> que;
        if (n == k) {
            printf("Case #%d: 0 0\n", _ + 1);
            continue;
        }
        que.push(n);
        for (int i = 0; i < k; i++) {
            int len = que.top(); que.pop();
            que.push((len - 1) / 2);
            que.push((len - 1) / 2 + (len - 1) % 2);
            if (i + 1 == k) {
                a1 = (len - 1) / 2 + (len - 1) % 2;
                a2 = (len - 1) / 2;
            }
        }
        // ll a1 = 0, a2 = LLONG_MAX;
        // for (auto x : s) {
        //     a1 = max(a1, x.len);
        //     a2 = min(a2, x.len);
        // }
        printf("Case #%d: %d %d\n", _ + 1, a1, a2);
    }
    resetfile();
    return 0;
}