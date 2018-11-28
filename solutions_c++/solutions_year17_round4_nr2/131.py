#include <bits/stdc++.h>

#define foreach(i,v) for(auto&& i: v)
#define all(x) (x).begin(), (x).end()

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

template <class C> C& mini(C& a, C b) { if (b < a) a = b; return a; }
template <class C> C& maxi(C& a, C b) { if (a < b) a = b; return a; }

using namespace std;

bool good(const VI& P, int m) {
    int f = 0;
    foreach (p, P) {
        f += m - p;
        if (f < 0)
            return false;
    }
    return true;
}

int fcp(const VI& P, int m) {
    int r = 0;
    foreach (p, P) {
        r += max(0, p - m);
    }
    return r;
}

int main(int argc, const char* argv[]) {
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        int N, C, M;
        scanf("%d%d%d", &N, &C, &M);
        VI P(N), B(C);
        for (int i = 0; i < M; i++) {
            int p, b;
            scanf("%d%d", &p, &b);
            P[p-1]++;
            B[b-1]++;
        }
        int mn = 0, mx = M;
        foreach (b, B)
            maxi(mn, b);
        mn--;
        while (mn + 1 < mx) {
            int md = (mn + mx) / 2;
            if (good(P, md))
                mx = md;
            else
                mn = md;
        }
        printf("Case #%d: %d %d\n", t, mx, fcp(P, mx));
    }
    return 0;
}
