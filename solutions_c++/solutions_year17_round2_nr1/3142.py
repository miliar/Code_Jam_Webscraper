#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long t, d, n;
    cin >> t;
    for (long long j = 0; j < t; ++j) {
        double max_time = 0;
        cin >> d >> n;
        for (long long i = 0; i < n; ++i) {
            long long ki, si;
            cin >> ki >> si;
            double cur_time = double(d - ki) / si;
            if (cur_time > max_time) {
                max_time = cur_time;
            }
        }
        double max_speed = double(d) / max_time;
      //int r = (long long)(max_speed * 1000000) % 10;
      //if (r > 4) {
      //    max_speed -= 0.000001;
      //}
        cout.precision(6);
        cout << "Case #" << j + 1 << ": " << fixed << max_speed << endl;

    }

    return 0;
}
