#include <iostream>
#include <fstream>

using namespace std;

ifstream in("C-large.in");
ofstream out("C-large.out");

//#define out cout

int main() {
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        unsigned long long n, k, power = 1;
        in >> n >> k;
        unsigned long long min_val = n, max_val = n, min_num = 0, max_num = 1;
        while (true) {
            if (k > power) {
                k -= power;
            } else {
                unsigned long long stalls;
                if (k <= max_num) stalls = max_val;
                else stalls = min_val;
                out << "Case #" << i + 1 << ": "
                    << stalls / 2 << ' ' << (stalls - 1) / 2 << '\n';
                break;
            }
            if (max_val % 2 == 0) {
                if (min_val % 2 == 0) min_num = max_num;
                else min_num += min_num + max_num;
            } else {
                if (min_val % 2 == 0) max_num += min_num + max_num;
                else max_num *= 2;
            }
            min_val = (min_val - 1) / 2;
            max_val = max_val / 2;
            power *= 2;
        }
    }
    return 0;
}
