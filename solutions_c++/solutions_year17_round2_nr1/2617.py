#include <cstdio>
#include <iostream>

using namespace std;

double solve() {
    int N, D;
    scanf("%d %d", &D, &N);
    double max_time;
    for (int i = 0; i < N; i++) {
        int pos;
        double speed, time;
        scanf("%d %lf", &pos, &speed);
        time = (D - pos) / speed;
        if (i == 0) {
            max_time = time;
        } else {
            max_time = max(time, max_time);
        }
        // printf("%.2lf\n", min_time);
    }
    return D / max_time;
}

int main() {
    int TC;
    scanf("%d", &TC);
    
    for (int t = 1; t <= TC; t++) {
        printf("Case #%d: %.6lf\n", t, solve());
    }
}