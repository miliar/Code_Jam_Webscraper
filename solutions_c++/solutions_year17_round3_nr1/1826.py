#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#pragma warning(disable : 4267)
#pragma warning(disable : 4305)
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define PI (3.14159265358979323846)
#define F_INF 1e100

#define MAT(T, mat, N, M, value) vector<vector<T>> mat; mat.resize(N); for(auto& r: mat) r.resize(M, value);
#define FORN(i, n) for(int i = 0; i < (int)(n); ++i)

int N, K;

struct Cake {
    double R, H;
    Cake(double r = 0, double h = 0) : R(r), H(h) {}
    double value() const {
        return PI * R * (R + 2.0 * H);
    }

    bool operator < (const Cake& rhs) {
        if (R < rhs.R) return true;
        if (R == rhs.R) return H < rhs.H;
        return false;
    }
};

double solve(vector<Cake>& C, int Z) {
    double ans = PI * C[Z].R * (C[Z].R + 2.0 * C[Z].H);
    if (K == 1) return ans;

    vector<double> W;
    FORN(i, N)
        if (i != Z)
            W.push_back(2.0 * PI * C[i].R * C[i].H);
    sort(W.rbegin(), W.rend());

    FORN(i, K - 1)
        ans += W[i];
    return ans;
}

int main() {
    int T;  cin >> T;
    FORN(t, T) {
        cin >> N >> K;
        vector<Cake> C(N);
        FORN(i, N) cin >> C[i].R >> C[i].H;
        
        double ans = 0;
        FORN(i, N)
            ans = max(ans, solve(C, i));

        cout << "Case #" << (t + 1) << ": " << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}
