#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

ofstream out("tttt");

const long long N = 105;
const long long inf = (1LL<<60);

long long n, q, e[N], s[N], d[N][N];
double r[N][N];

void sol() {
    long long i, j;

    cin >> n >> q;
    memset(e, 0, sizeof(e));
    memset(s, 0, sizeof(s));
    memset(d, 0, sizeof(d));
    memset(r, 0, sizeof(r));

    for(i = 1; i <= n; ++i)
        cin >> e[i] >> s[i];

    for(i = 1; i <= n; ++i)
        for(j = 1; j <= n; ++j) {
            cin >> d[i][j];
            if(d[i][j] == -1)
                d[i][j] = inf;
        }

    for(long long k = 1; k <= n; ++k)
        for(i = 1; i <= n; ++i)
            for(j = 1; j <= n; ++j)
                if(d[i][j] > d[i][k] + d[k][j]) {

                    d[i][j] = d[i][k] + d[k][j];
                }

    for(i = 1; i <= n; ++i)
        for(j = 1; j <= n; ++j) {
            r[i][j] = 1.0 * d[i][j] / s[i];
            if(d[i][j] > e[i])
                r[i][j] = 1.0 * inf;
        }

    for(long long k = 1; k <= n; ++k)
        for(i = 1; i <= n; ++i)
            for(j = 1; j <= n; ++j)
                if(r[i][j] > r[i][k] + r[k][j]) {

                    r[i][j] = r[i][k] + r[k][j];
                }

    for(i = 1; i <= q; ++i) {
        long long u, v;
        cin >> u >> v;

        out << fixed << setprecision(11) << r[u][v] << " ";
    }
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    long long t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ": ";
        sol();
		out << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
