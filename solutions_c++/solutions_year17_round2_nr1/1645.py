#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int speeds[1001];
int pos[1001];

void solve() {
    int D, N;
    scanf("%d %d", &D, &N);

    for(int i = 0; i < N; ++i) {
        scanf("%d %d", &pos[i], &speeds[i]);
    }

    double max_speed = 100000000000000;
    for(int i = 0; i < N; ++i) {
        double time = (D - pos[i]) * 1.0 / speeds[i];
        if(D / time < max_speed)
            max_speed = D / time;
    }

    printf("%f\n", max_speed);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
