#include <cstdio>
#include <vector>
#include <set>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int _ = 1; _ <= t; _++) {
        int n, p;
        scanf("%d %d", &n, &p);
        vector<int> unit(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &unit[i]);
        }
        vector<vector<int>> packages(n, vector<int>(p));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &packages[i][j]);
            }
            sort(packages[i].begin(), packages[i].end());
        }
        vector<int> current_combo(n);
        vector<int> package_positions(n);
        int done = false;
        int result = 0;
        while (!done) {
            for (int i = 0; i < n; i++) {
                current_combo[i] += unit[i];
            }

            int can_make = 1 << 30;
            for (int i = 0; i < n; i++) {
                int low = (int) ceil(current_combo[i] * 0.9);
                int high = (int) floor(current_combo[i] * 1.1);
                while (package_positions[i] < p && packages[i][package_positions[i]] < low) {
                    package_positions[i]++;
                    if (package_positions[i] == p) {
                        done = true;
                    }
                }

                int this_can_make = 0;
                for (int j = package_positions[i]; j < p && packages[i][j] <= high; j++) {
                    this_can_make++;
                }

                can_make = min(can_make, this_can_make);
            }

            result += can_make;
            for (int i = 0; i < n; i++) {
                package_positions[i] += can_make;
                if (package_positions[i] == p) {
                    done = true;
                }
            }
        }

        printf("Case #%d: %d\n", _, result);
    }
    return 0;
}