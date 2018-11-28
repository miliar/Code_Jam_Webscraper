#include <iostream>
#include <map>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; ++i)
#define RANGE(i, x, n) for(int i = x; i < n; ++i)

typedef long long LL;
typedef long double LD;

//constexpr LD pi() { return std::atan(1)*4.0; }
const LD pi = 3.141592653589793238462643383279502884L;

struct Cake {
    int R;
    int H;
    double v;
    bool operator <(const Cake &r) const {
        return (R == r.R ? H < r.H : R < r.R);
    }
    bool operator >(const Cake &r) const {
        return (R == r.R ? H > r.H : R > r.R);
    }
    void getv() {
        v = 2 * pi * R * H;
    }
};

const LD INF = 1e20;
LD dp[1001][1001];

LD solve(int n, int k, int N, int K, vector<Cake> &cakes, bool begin)
{
    if(k == 0) {
        return 0;
    }
    if(n == N && k > 0) {
        return -INF;
    }
    if(dp[n][k] != 0) {
        return dp[n][k];
    }
    dp[n][k] = max(solve(n + 1, k, N, K, cakes, begin), solve(n + 1, k - 1, N, K, cakes, false) + cakes[n].v + (begin ? pi * cakes[n].R * cakes[n].R : 0));
    return dp[n][k];
}

int main()
{
    /*ios::sync_with_stdio(false);
    cin.tie(0);*/
    int T;
    cin >> T;
    RANGE(q, 1, T + 1) {
        memset(dp, 0, sizeof dp);
        int N, K;
        cin >> N >> K;
        vector<Cake> cakes(N);
        REP(i, N) {
            cin >> cakes[i].R >> cakes[i].H;
            cakes[i].getv();
        }
        sort(cakes.begin(), cakes.end(), greater<Cake>());
        LD ans = 0;
        //ans += pi * cakes[0].R * cakes[0].R;
        /*ans += cakes[0].v;
        cout << ans << endl;
        cakes.erase(cakes.begin());*/
        /*sort(cakes.begin(), cakes.end(), [](Cake a, Cake b) {
            return a.v > b.v;
        });*/
        ans += solve(0, K, N, K, cakes, true);
        cout << "Case #" << q << ": " << setprecision(20) << ans << endl;
    }
}
