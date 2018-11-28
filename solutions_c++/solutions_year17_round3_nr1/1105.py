#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <cmath>

using namespace std;

void doit() {
    int N, K;
    cin >> N >> K;
    vector<pair<long double, long double>> pancakes(N);
    for (int i = 0; i < N; ++i) {
        int R, H;
        cin >> R >> H;


        long double side = 2.0L * M_PIl * R * H;
        long double top = M_PIl * R * R;

        pancakes[i].first = side;
        pancakes[i].second = top;
    }
    sort(pancakes.rbegin(), pancakes.rend());

    long double best = 0.0;
    for (int i = 0; i < N; ++i) {
        long double cur = pancakes[i].first + pancakes[i].second;

        for (int j = 1, pidx = 0; j < K; ++j, pidx++) {
            if (pidx == i) {
                pidx++;
            }

            cur += pancakes[pidx].first;
        }

        if (cur > best) {
            best = cur;
        }
    }

    cout << best << endl;
}

int main() {
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        doit();
    }
    return 0;
}
