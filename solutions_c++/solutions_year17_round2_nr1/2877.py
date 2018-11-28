#include <algorithm>
#include <vector>
#include <utility>
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAXN = 1005;
    //const long double INF = 1000000.0L;
    int T;
    int D, N;
    long double K[MAXN], S[MAXN];
    cin >> T;
for(int kase = 1; kase <= T; ++kase) {
    cin >> D >> N;
    vector<long double> horses;
    for(int i = 0; i < N; ++i) {
        cin >> K[i] >> S[i];
        horses.push_back((D-K[i])/S[i]);
    }
    sort(horses.begin(),horses.end());
    cout << setprecision(12) << "Case #" << kase << ": " << D/horses[N-1] << endl;
}
    return 0;
}
