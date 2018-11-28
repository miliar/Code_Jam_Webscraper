#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;


double process(int D, vector< pair<int, int> > &horses) {
    double last = 0;

    for (auto &horse : horses) {
        last = max(last, (D - horse.first) / (double) horse.second);
    }

    return D / last;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test ++) {
        int D, N;
        scanf("%d %d", &D, &N);
        
        vector< pair<int, int> > horses(N);
        for (int i = 0; i < N; i ++) {
            scanf("%d %d", &horses[i].first, &horses[i].second);
        }

        printf("Case #%d: %.10lf\n", test, process(D, horses));
    }
    return 0;
}
