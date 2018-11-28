#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const double PI = 3.1415926535897932384626433832795;

struct PC
{
    uint32_t    r;
    uint32_t    h;
    uint64_t    aface;
    uint64_t    aside;

    PC();
};

PC::PC()
{
    r = 0;
    h = 0;
    aface = 0;
    aside = 0;
}

class Q
{
public:
    void solve(uint32_t tcnum);
};

void Q::solve(uint32_t tcnum)
{
    uint32_t i;

    uint32_t npcs;
    uint32_t k;
    cin >> npcs >> k;
    vector<PC> pcs(npcs);
    for (i = 0; i < npcs; ++i) {
        PC &pc = pcs[i];
        cin >> pc.r >> pc.h;
        pc.aface = static_cast<uint64_t>(pc.r) * pc.r;
        pc.aside = 2 * static_cast<uint64_t>(pc.r) * pc.h;
    }
    uint64_t max_aface = 0;
    uint64_t sum_sides = 0;
    for (i = 0; i < k; ++i) {
        uint64_t max_fs = 0;
        vector<PC>::iterator max_itr;
        for (auto itr = pcs.begin(); itr != pcs.end(); ++itr) {
            uint64_t fs = max(max_aface, itr->aface) + sum_sides + itr->aside;
            if (fs > max_fs) {
                max_fs = fs;
                max_itr = itr;
            }
        }
        max_aface = max(max_aface, max_itr->aface);
        sum_sides += max_itr->aside;
        pcs.erase(max_itr);
    }
    double area = PI * (max_aface + sum_sides);
    cout << "Case #" << tcnum << ": " << area << "\n";
}

int
main()
{
    uint32_t i;

    cout << fixed;
    cout.precision(8);

    uint32_t ntc;
    cin >> ntc;
    for (i = 1; i <= ntc; ++i) {
        Q().solve(i);
    }

    return 0;
}
