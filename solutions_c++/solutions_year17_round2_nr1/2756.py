#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream in("a.in");
    ofstream out("a.out");
    int T = -1;
    in >> T;
    for (int t = 0; t < T; ++t) {
        uint32_t n, d;
        in >> d >> n;
        double max_time = 0;
        for (size_t i = 0; i < n; ++i) {
            uint32_t k, s;
            in >> k >> s;
            double arr_tm = static_cast<double>(d - k) / s;
            if (arr_tm > max_time)
                max_time = arr_tm;
        }
        out << fixed;
        out << "Case #" << (t + 1) << ": " << d / max_time;
        out << '\n';
    }
    return 0;
}
