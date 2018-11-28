#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main () {
    int nc;

    cin >> nc;
    for (int tc = 1; tc <= nc; tc++) {
        cout << "Case #" << tc << ": ";

        int D;
        int N;
        cin >> D >> N;
        double maxf = 0;
        for (int i = 0; i < N; i++) {
            int k, s;
            cin >> k >> s;
            double f = (double)(D - k) / s;
            if (maxf < f) maxf = f;
        }
        printf("%.6lf\n", D / maxf);
    }
    return 0;
}