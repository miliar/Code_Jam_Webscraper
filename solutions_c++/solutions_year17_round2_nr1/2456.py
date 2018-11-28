#include <bits/stdc++.h>

using namespace std;

typedef pair<double, double> pd;

int N;
double D;

double calc_time(double pos, double speed) {
    return (D - pos) / speed;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> D >> N;
        double pos, speed;
        cin >> pos >> speed;
        double time_slowest = calc_time(pos, speed);
        for (int i = 1; i < N; i++) {
            cin >> pos >> speed;
            time_slowest = max(time_slowest, calc_time(pos, speed));
        }

        printf("Case #%d: %0.8lf\n", t, D / time_slowest);
    }
    return 0;
}
