#include <cstdio>
#include <iostream>
#include <iomanip>
#include <vector>

typedef long double ld;
using namespace std;

int main() {
    int testcount; scanf("%d", &testcount);
    int test_id = 0;
    while (testcount > 0) { testcount--; test_id += 1;
        ld l = 0, r = 1e30;
        
        int d, n; scanf("%d %d", &d, &n);
        vector<int> k(n), s(n);

        for(int i = 0; i < n; i++) scanf("%d %d", &k[i], &s[i]);

        for(int iter = 0; iter < 300; iter++) {
            ld mid = (r + l) / 2.0;
            bool bad = false;
            for(int i = 0; i < n; i++) {
                if (bad) break;
                int K = k[i]; int S = s[i];
                ld myHorse = d / mid;
                ld anotherHorse = (d - K) / ld(S);
                if (myHorse < anotherHorse) {
                    bad = true;
                }
            }

            if (bad) {
                r = mid;
            } else {
                l = mid;
            }
        }
        cout << fixed << setprecision(12) << "Case #" << test_id << ": " << l << endl; 
    }
}
