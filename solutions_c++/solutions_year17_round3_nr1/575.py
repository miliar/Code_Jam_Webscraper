#include <iostream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <limits>
#include <cassert>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>
#include <math.h>


double solve()
{
    return 0;
}

struct pancake
{
    long r;
    long h;
    long circular_area;  // without factor pi
    long cylindric_area;  // without factor pi
    long value;
    bool chosen;
};


void run_test_case()
{
    size_t N, K;
    std::cin >> N >> K;

    /* std::vector<long> R(N); */
    /* std::vector<long> H(N); */
    /* std::vector<long> circular_area; */
    /* std::vector<long> cylindric_area; */
    std::vector<pancake> ps;
    /* std::cout << '\n' << "N = " << N <<";   K = " <<K <<'\n'; */

    for (size_t i = 0; i < N; ++i) {
        pancake p;
        std::cin >> p.r >> p.h;
        p.circular_area = p.r * p.r;
        p.cylindric_area = 2 * p.r * p.h;
        p.value = p.circular_area + p.cylindric_area;
        p.chosen = false;
        /* std::cout << "got: " << p.r << "  " << p.h <<  "    ci=" << p.circular_area << "   cy=" << p.cylindric_area << '\n'; */

        ps.push_back(p);
/*         /1* circular_area.push_back(static_cast<double>(R[i] * R[i]) * M_PI); *1/ */
/*         /1* cylindric_area.push_back(static_cast<double>(2 * R[i] * H[i]) * M_PI); *1/ */
/*         circular_area.push_back(R[i] * R[i]); */
/*         cylindric_area.push_back(2 * R[i] * H[i]); */
    }

    long area = 0;

    // the total circular area depends only on the largest (lowest) pancake
    // so, first we simply choose according to the heights
    std::sort(ps.begin(), ps.end(), [](pancake p1, pancake p2) { return p1.cylindric_area > p2.cylindric_area; });

    long cur_base_r = 0;
    for (size_t i = 0; i < K - 1; ++i) {
        pancake& p = ps[i];
        assert(!p.chosen);
        area += p.cylindric_area;
        p.chosen = true;
        /* std::cout << "choose " << p.r << " " << p.h << '\n'; */
        if (p.r > cur_base_r) {
            cur_base_r = p.r;
        }
    }

    for (pancake& p : ps) {
        /* std::cout << "pancake: " << p.r << "  " << p.h <<  "   chosen? " << p.chosen <<'\n'; */

        if (!p.chosen) {
            if (p.r > cur_base_r) {
                p.value = p.circular_area + p.cylindric_area;
            } else {
                p.value = p.cylindric_area + (cur_base_r * cur_base_r);
            }
        } else {
            p.value = -1;
        }
    }

    // Now to find the best pancake as "base"
    std::sort(ps.begin(), ps.end(), [](pancake p1, pancake p2) { return p1.value > p2.value; });
    {
        pancake& p = ps.front();
        assert(!p.chosen);
        area += p.value;
        p.chosen = true;
        /* std::cout << "choose as base " << p.r << " " << p.h << '\n'; */
        /* if (!p.chosen) { */
        /*     // this must also have greater radius than the ones already chosen (otherwise it would've been selected earlier already) */
        /*     for (pancake const& p2 : ps) { if (p2.chosen) assert(p.r >= p2.r); } */
        /*     p.chosen = true; */
        /*     area += p.value; */
        /*     std::cout << "choose as base " << p.r << " " << p.h << '\n'; */
        /* } */
        /* else { */
        /*     // best base already chosen? just select another according to height */
        /*     std::sort(ps.begin(), ps.end(), [](pancake p1, pancake p2) { return p1.cylindric_area > p2.cylindric_area; }); */
        /*     for (pancake& p2 : ps) { */
        /*         if (!p2.chosen) { */
        /*             area += p2.cylindric_area; */
        /*             p2.chosen = true; */
        /*             std::cout << "choose as base2 " << p2.r << " " << p2.h << '\n'; */
        /*             std::sort(ps.begin(), ps.end(), [](pancake a, pancake b) { return a.r > b.r; }); */
        /*             for (pancake const& p3 : ps) { */
        /*                 if (p3.chosen) { */
        /*                     area += p3.circular_area; */
        /*                     break; */
        /*                 } */
        /*             } */
        /*             break; */
        /*         } */
        /*     } */
        /* } */
    }

    /* std::cout << area << ' '; */

    double result = static_cast<double>(area) * M_PI;
    printf("%.9f", result);
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
