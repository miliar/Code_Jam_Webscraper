#include <iostream>
#include <fstream>
#include <cstdint>

using namespace std;

int main() {
    int T = -1;
    ifstream in("a.in");
    ofstream out("a.out");
    in >> T;
    for (int t = 0; t < T; ++t) {
        uint64_t n;
        in >> n;
        int dig_num = 0;
        uint64_t step = 0;
        uint64_t m = n;
        while (m > 0) {
            step = step * 10 + 1;
            m /= 10;
        }

        uint64_t tidy = 0;
        int cnt = 0;
        while (step > 0 && cnt < 9) {
            while (tidy + step <= n && cnt < 9) {
                ++cnt;
                tidy += step;
            }
            step /= 10;
        }
        out << "Case #" << t + 1 << ": " << tidy;
        out << endl;
    }
    return 0;
}
