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
    std::uint64_t k = 0;
    
    std::fscanf(ifile, "%d %d", &n, &k);

    auto base = k + 1;
    while(0 != ((base- 1) & base))
        base &= (base- 1);

    if(base == k + 1)
        base >>= 1;

    auto range_no = base;
    auto na = (n - base + 1);
    auto range_size = na / range_no;
    auto diff = na - range_size * range_no;
    auto range_id = k - base;
    auto space = range_id < diff ? range_size + 1 : range_size;
    --space;

    auto min = space / 2;
    auto max = (space + 1) / 2;

    ofile << "Case #" << _case << ": " << max << " " << min << "\n";
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
