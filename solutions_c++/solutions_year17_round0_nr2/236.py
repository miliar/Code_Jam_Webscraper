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

int64_t getPlaceValue(int place) {
    int64_t placeValue = 1;
    for (int i = place; i > 0; --i)
        placeValue *= 10;
    return placeValue;
}

int64_t getDigit(int64_t n, int place) {
    return (n / getPlaceValue(place)) % 10;
}

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    int64_t n;
    cin >> n;
    
    for (int i = 0; i < 18; ++i) {
        if (getDigit(n, i+1) > getDigit(n, i)) {
            n = n - (n % getPlaceValue(i+1)) - 1;
        }
    }
    
    cout << n << "\n";
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