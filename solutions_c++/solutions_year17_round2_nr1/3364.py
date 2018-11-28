#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <tuple>
#include <queue>
#include <string>
#include <cmath>

using namespace std;

double solve(int D, vector<tuple<int, int>>& horses) {
    sort(horses.begin(), horses.end());

    int min_speed = get<1>(horses[0]);
    double curr_position = get<0>(horses[0]);
    double total_taken = ((double)D - curr_position) / min_speed;

    for (int i = 1; i < horses.size(); ++i) {
        int speed = get<1>(horses[i]);
        int position =  get<0>(horses[i]);
        double taken = ((double)D - position) / speed;

        if (taken < total_taken)
            continue;

        total_taken = taken;
    }


    return D / total_taken;
}

int main() {
    int T;
    cin >> T;

    for (int kase = 1; kase <= T; ++kase) {
        int D, N;
        cin >> D >> N;

        vector<tuple<int, int>> horses(N);

        for (int i = 0; i < N; ++i) {
            int ki, si;
            cin >> ki >> si;
            horses[i] = make_tuple(ki, si);
        }

        printf("Case #%d: %lf\n", kase, solve(D, horses));
    }

    return 0;
}
