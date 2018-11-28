//
//  tidy.cpp
//  codejam
//
//
#include <stdio.h>
#include <iostream>
#include <sstream>

std::string checkTidy(std::string &s)
{
    const int len = s.length();
    int idx = len;
    for (int i=len-1; i>0; i--) {
        int last = s[i]-'0';
        int prev = s[i-1]-'0';
        if (last < prev) { idx = i; s[i-1] = ('0'+prev-1); }
    }
    for (int i=idx; i<len; i++) { s[i] = '9'; }
    if (s[0] == '0') { s=s.substr(1);}
    return s;
}

int main() {
    int tests = 0;
    std::cin >> tests;
    for (int i=1;i<=tests;i++) {
        std::string s; int k;
        std::cin >> s;
        std::cout << "Case #" << i << ": " << checkTidy(s) <<  std::endl;
    }
    return 0;
}
