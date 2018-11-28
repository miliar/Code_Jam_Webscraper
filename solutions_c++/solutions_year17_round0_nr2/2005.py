﻿
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <ctime>
#include <chrono>
#include <cstdint>
#include <vector>
#include <map>
#include <math.h>
#include <iomanip>
#include <iterator>
#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <bitset>
#include <queue>
#include <unordered_map>
#include <set>
#include <stack>
#include <fstream>

FILE * ifile = nullptr;
std::ofstream ofile;

#define MAX_N 1001

void solve(int _case) {
    std::uint64_t n = 0;

    std::fscanf(ifile, "%lld", &n);

    std::vector<int> number;

    while(0 != n) {
        number.push_back(n % 10);
        n /= 10;
    }

    auto a = number.front();
    auto index = -1;
    for(auto i = 1u; i < number.size(); ++i) {
        if(number[i] > a) {
            index = i;
            --number[i];
            a = number[i];
        } else {
            a = std::min(a, number[i]);
        }
    }

    if(-1 != index) {
        if(0 == number.back())
            number.pop_back();
        for(auto i = 0; i < index; ++i)
            number[i] = 9;
    }

    std::reverse(number.begin(), number.end());

    ofile << "Case #" << _case << ": ";
    for(auto v : number)
        ofile << v;
    ofile  << "\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    ifile = fopen("1.in","r");
    ofile.open("output.out");
    
    int n = 0;
    std::fscanf(ifile, "%d", &n);
    for(auto i = 0; i < n; ++i)
        solve(i + 1);

    ofile.close();

    return 0;
}
