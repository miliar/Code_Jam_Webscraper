#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <math.h>
using namespace std;

using dim_t = long long;
struct Pancake {
    dim_t R, H;
    dim_t sideArea() const {
        return 2 * R * H;
    }
    dim_t topArea() const {
        return R * R;
    }
};

dim_t chooseSideArea(vector<Pancake>& pancakes, int K) {
    // always choose the best contributor
    size_t bestContributor = 0;
    dim_t bestContribution = 0;
    for (size_t k = 0; k < pancakes.size(); ++k) {
        dim_t contribution = pancakes[k].topArea() + pancakes[k].sideArea();
        if (contribution > bestContribution) {
            bestContributor  = k;
            bestContribution = contribution;
        }
    }
    // location 1 is reserved for best contributor
    swap(pancakes[0], pancakes[bestContributor]);

    // choose the K-1 next pancakes with greatest side area
    sort(pancakes.begin() + 1, pancakes.end(), [](const Pancake& a, const Pancake& b) {
        if (a.sideArea() > b.sideArea()) {
            return true;
        }
        if (a.sideArea() == b.sideArea()) {
            return a.topArea() > a.topArea();
        }
        return false;
    });

    // find the bottom
    size_t bottomIndex  = 0;
    dim_t largestRadius = 0;
    for (int k = 0; k < K; ++k) {
        if (pancakes[k].R > largestRadius) {
            largestRadius = pancakes[k].R;
            bottomIndex   = k;
        }
    }

    // compare top area gain of introducing new guy to lowest contribution (to be replaced)
    dim_t currentTopArea = pancakes[bottomIndex].topArea();
    dim_t lowestSideArea = numeric_limits<dim_t>::max();
    dim_t replaced       = 0;
    for (int k = 1; k < K; ++k) {
        if (pancakes[k].sideArea() < lowestSideArea) {
            replaced       = k;
            lowestSideArea = pancakes[k].sideArea();
        }
    }

    // find a replacement
    int replacement = -1;
    for (int k = K; k < (int)pancakes.size(); ++k) {
        if (pancakes[k].topArea() > currentTopArea) {
            dim_t topAreaGain  = pancakes[k].topArea() - currentTopArea;
            dim_t sideAreaLoss = lowestSideArea - pancakes[k].sideArea();
            if (topAreaGain > sideAreaLoss) {
                replacement    = k;
                currentTopArea = pancakes[k].topArea();
                // guaranteed to have lower side area because coming from outside the k
                lowestSideArea = pancakes[k].sideArea();
            }
        }
    }
    if (replacement != -1) {
        swap(pancakes[replaced], pancakes[replacement]);
    }

    // {
    //     cout << endl;
    //     for (size_t i = 0; i < pancakes.size(); ++i) {
    //         const auto& p = pancakes[i];
    //         if ((int)i == K) {
    //             cout << "--------------\n";
    //         }
    //         cout << p.R << " " << p.H << "-> " << std::setw(15) << p.sideArea() << " + "
    //              << p.topArea() << endl;
    //     }
    // }

    dim_t sideAreas = 0;
    for (int k = 0; k < K; ++k) {
        sideAreas += pancakes[k].sideArea();
    }
    return sideAreas + currentTopArea;
}

int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; ++c) {
        int N, K;
        cin >> N >> K;
        vector<Pancake> pancakes;
        for (int n = 1; n <= N; ++n) {
            dim_t R, H;
            cin >> R >> H;
            pancakes.push_back({R, H});
        }

        // { cout << "\nD " << D << endl; }
        cout << "Case #" << c << ": " << std::fixed << std::setprecision(9)
             << chooseSideArea(pancakes, K) * M_PI << endl;
    }
}