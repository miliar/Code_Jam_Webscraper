#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

#define MAX_N 1005

double speeds[MAX_N];
double positions[MAX_N];
double D;
int N;

double solve() {
    double slowest = (D - positions[N-1]) / speeds[N-1];
    //cerr << "slowest " << slowest << endl;
    for (int i = N-2; i >= 0; i--) {
        double cur = (D - positions[i]) / speeds[i];

        slowest = max(cur, slowest);
    }

    return D / slowest;
}

int main() {
    int T; cin >> T;

    for (int ca = 1; ca <= T; ca++) {
        cin >> D >> N;
        vector< pair<double, double> > pairs;
        for (int i = 0; i < N; i++) {
            double position, speed;
            cin >> position >> speed;
            pairs.push_back(make_pair(position, speed));
        }

        sort(pairs.begin(), pairs.end());

        for (int i = 0; i < N; i++) {
            positions[i] = pairs[i].first;
            speeds[i] = pairs[i].second;
        }

        double res = solve();

        //cout << "Case #" << ca << ": " << res << endl;
        printf("Case #%d: %.7f\n", ca, res);
    }
    return 0;
}