#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>

using namespace std;

pair<int, int> cakes[1000];

void solve() {
    int N, K;
    scanf("%d %d", &N, &K);

    for(int i = 0; i < N; ++i) {
        scanf("%d %d", &cakes[i].first, &cakes[i].second);
    }

    double best = 0;
    sort(cakes, cakes + N);
    for(int i = K - 1; i < N; ++i) {
        double r_area = (double) cakes[i].first * (double) cakes[i].first;
        double h_area = 2 * (double) cakes[i].first * (double) cakes[i].second;

        vector<double> temp;
        for(int j = 0; j < i; ++j) {
            temp.push_back(2 * (double) cakes[j].first * (double) cakes[j].second);
        }
        sort(temp.begin(), temp.end());
        reverse(temp.begin(), temp.end());
        for(int j = 0; j < K - 1; ++j) {
            h_area += temp[j];
        }

        double cur = M_PI * (r_area + h_area);
        if(cur > best) best = cur;
    }
    printf("%.9lf\n", best);
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
