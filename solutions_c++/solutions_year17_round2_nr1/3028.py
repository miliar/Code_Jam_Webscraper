#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct {
    int k, v;
} HORSE;

bool sortHorses(const HORSE &h1, const HORSE &h2) {
    return h1.k < h2.k;
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int tests, D, N;
    double cruiseSpeed;
    vector<HORSE> horses;

    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        horses.clear();

        cin >> D >> N;
        for (int h = 0; h < N; ++h) {
            HORSE horse;
            cin >> horse.k >> horse.v;
            horses.push_back(horse);
        }

        sort(horses.begin(), horses.end(), sortHorses);

        cruiseSpeed = 9999999999999;
        for (int h = 0; h < N; ++h) {
            cruiseSpeed = min(cruiseSpeed, D / ((1.0 * D - horses[h].k) / horses[h].v));
        }

        printf("Case #%d: %lf\n", test, cruiseSpeed);
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
