#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#define EPS 1e-8
#define fi first
#define se second
using namespace std;
typedef long double myf;
typedef long long ll;
typedef pair<int, int> pii;
const int MAX = 10100;
myf rem;
int D, N, K, S;
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cout << setprecision(7) << fixed;
    int T;
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cin >> D >> N;
        myf ans = -1;
        for(int i = 0; i < N; ++i) {
            cin >> K >> S;
            rem = 1.0L * (D - K) / S;
            if(ans < 0 || D / rem < ans)
                ans = D / rem;
        }
        cout << "Case #" << test << ": " << ans << endl;
    }

    return 0;
}
