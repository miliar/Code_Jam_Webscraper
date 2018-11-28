#include <bits/stdc++.h>

#define foreach(i,v) for(auto&& i: v)
#define all(x) (x).begin(), (x).end()

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

template <class C> C& mini(C& a, C b) { if (b < a) a = b; return a; }
template <class C> C& maxi(C& a, C b) { if (a < b) a = b; return a; }

using namespace std;

int N, P;
int dp[128][128][128][4];

int solve(int m1, int m2, int m3, int last) {
    int& r = dp[m1][m2][m3][last];
    if (r >= 0)
        return r;
    r = 0;
    if (m1)
        maxi(r, solve(m1-1, m2, m3, (last + 1) % P));
    if (m2)
        maxi(r, solve(m1, m2-1, m3, (last + 2) % P));
    if (m3)
        maxi(r, solve(m1, m2, m3-1, (last + 3) % P));
    if (!last)
        r++;
    return r;
}

int main(int argc, const char* argv[]) {
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d", &N, &P);
        int M[4] = { };
        for (int i = 0; i < N; i++) {
            int x;
            scanf("%d", &x);
            M[x % P]++;
        }
        memset(dp, -1, sizeof(dp));
        for (int i = 0; i < 3; i++)
            dp[0][0][0][i] = 0;

        int r;
        r = solve(M[1], M[2], M[3], 0);

        printf("Case #%d: %d\n", t, M[0] + r);
    }
    return 0;
}
