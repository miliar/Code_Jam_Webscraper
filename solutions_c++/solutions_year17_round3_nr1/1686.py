#include "bits.h"
using namespace std;

typedef long long ll;

/*
template <typename T>
T max(T a, T b) {
    return a > b ? a : b;
}
*/

#define PI 3.14159265358979

double actuallySolve(vector<pair<ll,ll> > pancakes, int botIndex, int K) {
    ll R,H; R = pancakes[botIndex].first; H = pancakes[botIndex].second;
    double totArea = PI * (R*R + 2*R*H);
    pancakes.erase(pancakes.begin()+botIndex);
    K--;

    for (int i = 0; i < K; i++) {
        pair<ll,ll> currPancake = pancakes[i];
        totArea += currPancake.first * 2 * PI * currPancake.second;
    }
    return totArea;
}

void solve() {
    int N, K; cin >> N >> K;

    vector<pair<ll,ll> > pancakes;
    for (int i = 0; i < N; i++) {
        ll R, H; cin >> R >> H;
        pancakes.push_back(make_pair(R,H));
    }

    sort(pancakes.begin(), pancakes.end(), [](pair<ll,ll> lhs, pair<ll,ll> rhs) -> bool { return lhs.first*lhs.second > rhs.first*rhs.second; });
    
    double maxAns = -1;
    for (int i = 0; i < N; i++) {
        maxAns = max(maxAns, actuallySolve(pancakes, i, K));
    }

    cout << setprecision(16) << maxAns;
}

int main() {
    int T; cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
