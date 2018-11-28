//
// Created by Xuren Zhou on 22/4/2017.
//

#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i=1; i <= t; i++) {
        int d, n;
        cin >> d >> n;

        double max_time = -1;
        for(int j=0; j < n; j++) {
            int k, s;
            cin >> k >> s;
            double time = (double)(d - k)/(double)s;
            max_time = max(time, max_time);
        }

        printf("Case #%d: %.6lf\n", i, d/max_time);
    }
    return 0;
}