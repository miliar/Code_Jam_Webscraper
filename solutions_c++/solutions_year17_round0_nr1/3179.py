//
//  ihop.cpp
//  codejam
//
// Greedy ? Dynamic program ?
// Skip over first positives. Flip consecutive k.
//
#include <stdio.h>
#include <iostream>
#include <sstream>

std::string flipAndCheck(std::string &s, const int k)
{
    std::ostringstream oss;
    int flips = 0;
    int idx = 0;
    const int len = s.length();
    while (idx<len) {
        if (s[idx]=='+') { idx++; }
        if (s[idx]=='-') {
            if (idx+k <= len) {
                flips++;
                for (int i=0;i<k;i++) { s[idx+i] = ((s[idx+i]=='+') ? '-' : '+'); }
            } else {
                oss << "IMPOSSIBLE";
                return oss.str();
            }
        }
    }
    oss << flips;
    return oss.str();
}

int main() {
    int tests = 0;
    std::cin >> tests;
    for (int i=1;i<=tests;i++) {
        std::string s; int k;
        std::cin >> s >> k;
        std::cout << "Case #" << i << ": " << flipAndCheck(s,k) << std::endl;
    }
    return 0;
}
