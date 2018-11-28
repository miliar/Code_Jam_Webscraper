// Compile with MinGW-64 (6.3.0) in MSYS2
// Compile switches: -std=c++11 -Wall -Wconversion -Werror

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

int div_up(int n, int d) {
    return n/d + (n%d>0 ? 1 : 0);
}

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    int n, p;
    std::cin >> n >> p;

    std::vector<int> tours(p, 0);
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        
        tours[num % p]++;
    }
    
    int gps = 0;
    if (p == 2) {
        gps = tours[0] + div_up(tours[1], 2);
    } else if (p == 3) {
        gps = tours[0] + min(tours[1], tours[2]) + div_up(abs(tours[1]-tours[2]), 3);
    } else if (p == 4) {
        gps = tours[0] + min(tours[1], tours[3]) + div_up(abs(tours[1]-tours[3]) + tours[2] * 2, 4);
    } else {
        cerr << "wrong p value: " << p << "\n";
    }
    
    cout << gps << "\n";
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::getline(std::cin, str);

    for (int i = 0; i < N; ++i) {
        solve(i + 1);
    }

    return 0;
}