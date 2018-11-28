#include <bits/stdc++.h>

#define foreach(i,v) for(auto&& i: v)
#define all(x) (x).begin(), (x).end()

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

template <class C> C& mini(C& a, C b) { if (b < a) a = b; return a; }
template <class C> C& maxi(C& a, C b) { if (a < b) a = b; return a; }

using namespace std;

struct Horse {
    int e, s;
};

#define INF (1LL << 50)

int main(int argc, const char* argv[]) {
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        int N, Q;
        scanf("%d%d", &N, &Q);
        vector<Horse> H(N);
        foreach (x, H)
            scanf("%d%d", &x.e, &x.s);
        vector<vector<ll>> D(N);
        foreach (d, D) {
            d.resize(N);
            foreach (x, d) {
                scanf("%lld", &x);
                if (x < 0)
                    x = INF;
            }
        }
        for (int i = 0; i < N; i++)
            D[i][i] = 0;

        for (int k = 0; k < N; k++)
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    mini(D[i][j], D[i][k] + D[k][j]);

        vector<vector<double>> times(N, vector<double>(N));
        for (int i = 0; i < N; i++) {
            Horse h = H[i];
            for (int j = 0; j < N; j++)
                times[i][j] = (D[i][j] <= h.e ? (double)D[i][j] / h.s : 1e60);
        }

        for (int k = 0; k < N; k++)
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    mini(times[i][j], times[i][k] + times[k][j]);
        printf("Case #%d:", t);
        while (Q --> 0) {
            int u, v;
            scanf("%d%d", &u, &v);
            printf(" %.9f", times[u-1][v-1]);
        }
        printf("\n");
    }
    return 0;
}
