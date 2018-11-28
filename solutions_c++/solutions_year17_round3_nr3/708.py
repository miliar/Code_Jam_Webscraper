//
//  fox.cpp
//  mepcpp
//
//  Created by Zinge on 5/28/16.
//  Copyright © 2016 MEP. All rights reserved.
//

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#ifndef LOCAL_JUDGE_
const int max_n = 110;
#else  // LOCAL_JUDGE_
const int max_n = 110;
#endif // LOCAL_JUDGE_

void redirect_input(const std::string& path) {
    std::freopen(path.c_str(), "r", stdin);
}

void redirect_output(const std::string& path) {
    std::freopen(path.c_str(), "w", stdout);
}

double p[max_n];

int main() {
#ifdef LOCAL_JUDGE_
    redirect_input("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/in");
    redirect_output("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/out");
#endif // LOCAL_JUDGE_

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int n, k;
        std::cin >> n >> k;

        double u;
        std::cin >> u;

        for (int i = 1; i <= n; ++i) {
            std::cin >> p[i];
        }

        std::sort(p + 1, p + n + 1);

        double avg = 0;
        double low = 0;
        double high = 1;
        for (int i = 1; i <= 100; ++i) {
            auto mid = (low + high) / 2;
            double need = 0;
            for (int j = 1; j <= n; ++j) {
                if (p[j] < mid) {
                    need += mid - p[j];
                }
            }
            if (need <= u) {
                avg = mid;
                low = mid;
            } else {
                high = mid;
            }
        }

        double prob = 1;
        for (int i = 1; i <= n; ++i) {
            prob *= std::max(avg, p[i]);
        }

        std::cout << "Case #" << ti << ": " << std::fixed
                  << std::setprecision(10) << prob << std::endl;
    }
}
