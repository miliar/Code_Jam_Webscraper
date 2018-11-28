#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>


using namespace std;


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output", "w", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int64_t d, n;
        cin >> d >> n;

        double time = -123123;
        for (int i = 0; i < n; i++) {
            int64_t k, s;
            cin >> k >> s;

            double dist = (d - k);
            if (dist / s > time) {
                time = dist / s;
            }
        }

        printf("Case #%d: %.7f\n", t + 1, d / time);
    }

    return 0;
}
