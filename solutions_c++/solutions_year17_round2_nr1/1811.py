#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#pragma warning(disable : 4244)
#pragma warning(disable : 4267)
#pragma warning(disable : 4305)
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
#define INF 18000000000000000
#define F_INF 1e100

ull N;
double D;
vector<pair<double, double>> K;

double solve() {
    double w = 0;
    for (auto& k : K) {
        w = max(w, (D - k.first) / k.second);
    }
    return D / w;
}

int main() {
    int T;  cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> D >> N;
        K.resize(N);
        for (int i = 0; i < N; ++i)
            cin >> K[i].first >> K[i].second;

        sort(K.begin(), K.end());

        cout << fixed << setprecision(0) << "Case #" << t << ": " << setprecision(7) << solve() << endl;
    }
    return 0;
}

