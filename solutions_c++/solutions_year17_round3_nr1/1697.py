
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

#define MAX_N 1000
#define PI 3.141592653589793238L

struct pancake {
    int r {0};
    int h {0};
    int id {0};
    long double area_h {0};
    long double area_v {0};
    long double area_t {0};
    long double area_a {0};
};

pancake pancakes[MAX_N];


void solve(int _case) {

    int n, k;
    pancake *max_p = nullptr;
    long double result = 0;;
    bool visite[MAX_N];

    std::fscanf(ifile, "%d %d", &n, &k);

    for(auto i = 0; i < n; ++i) {
        auto& p = pancakes[i];
        std::fscanf(ifile, "%d %d", &p.r, &p.h);
        p.area_v = 2 * PI * p.r * p.h;
        p.area_h = PI * p.r * p.r;
        p.area_t = p.area_v + p.area_h;
        p.id = i;
        if((0 == i) || (max_p->area_t < p.area_t))
            max_p = &pancakes[i];
        visite[i] = false;
    }

    /*
    for(auto i = 0; i < n; ++i) {
        auto& p = pancakes[i];
        ofile << "--- " << p.area_t << " " << p.area_h << " " << p.area_v << "\n";
    }
    */

    result = max_p->area_t;
    visite[max_p->id] = true;
    --k;
    long double max_area_h = max_p->area_h;
    while(k--) {
        pancake *next = nullptr;
        for(auto i = 0; i < n; ++i) {
            if(visite[i]) continue;
            auto& p = pancakes[i];
            p.area_a = p.area_h - max_area_h;
            if(0 > p.area_a) p.area_a = 0;
            p.area_a += p.area_v;
            if(nullptr == next) {
                next = &pancakes[i];
                continue;
            }
            if(p.area_a > next->area_a)
                next = &pancakes[i];
        }
        max_area_h = std::max(max_area_h, next->area_h);
        result += next->area_a;
        visite[next->id] = true;
    }

    ofile << "Case #" << _case << ": " << result << "\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    ifile = fopen("1.in","r");
    ofile.open("output.out");
    ofile << std::setprecision(9) << std::fixed;
    
    int n = 0;
    std::fscanf(ifile, "%d", &n);
    for(auto i = 0; i < n; ++i)
        solve(i + 1);

    ofile.close();

    return 0;
}
