#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <limits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        int D, N;
        long K, S;
        double ans = numeric_limits<double>::infinity(), time;

        cin >> D >> N;
        for (int i = 0; i < N; ++i) {
            cin >> K >> S;
            time = (double) D * S / (D - K);
            if (time < ans) {
                ans = time;
            }
        }

        printf("Case #%d: %.6f\n", t, ans);
    }

    return 0;
}
