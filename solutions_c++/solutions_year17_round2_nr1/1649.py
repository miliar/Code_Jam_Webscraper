//
// Created by andy on 4/22/17.
//

#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <sstream>

using namespace std;



int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int n, d;
        cin >> d >> n;
        double s = 1e307;
        for (int j = 0; j < n; j++) {
            int k, cur_s;
            cin >> k >> cur_s;

            double max_t = (d - k) / double(cur_s);
            s = min(s, k / max_t + cur_s);
        }
        cout << "Case #" << i + 1 << ": " << std::setprecision(7) << s << endl;
    }

    return 0;
}
