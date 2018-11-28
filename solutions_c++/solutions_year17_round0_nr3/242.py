// Compile with MinGW-64 (6.3.0) in MSYS2

#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    int64_t n, k;
    cin >> n >> k;

    int64_t size_a = n;
    int64_t count_a = 1;
    int64_t count_b = 0;

    int64_t i;
    for (i = 1; i < k; i = i * 2 + 1) {
        if (size_a % 2 == 1) {
            count_a = count_a * 2 + count_b;
        } else {
            count_b = count_b * 2 + count_a;
        }
        size_a /= 2;
    }

    int64_t allot_size = (k <= i - count_b) ? size_a : size_a - 1;
    //cerr << allot_size << " " << i << "\n";
    cout << (allot_size / 2) << " " << ((allot_size-1) / 2) << "\n";
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::getline(std::cin, str);

    for(int i = 0; i < N; ++i) {
        solve(i + 1);
    }

    return 0;
}