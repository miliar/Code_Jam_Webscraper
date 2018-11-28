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
const int max_n = 220;
#else  // LOCAL_JUDGE_
const int max_n = 220;
#endif // LOCAL_JUDGE_

void redirect_input(const std::string& path) {
    std::freopen(path.c_str(), "r", stdin);
}

void redirect_output(const std::string& path) {
    std::freopen(path.c_str(), "w", stdout);
}

std::pair<int, int> a[max_n], b[max_n];

int main() {
#ifdef LOCAL_JUDGE_
    redirect_input("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/in");
    redirect_output("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/out");
#endif // LOCAL_JUDGE_

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int n, m;
        std::cin >> n >> m;

        for (int i = 1; i <= n; ++i) {
            std::cin >> a[i].first >> a[i].second;
        }
        for (int i = 1; i <= m; ++i) {
            std::cin >> b[i].first >> b[i].second;
        }

        int ans = 1e9;
        for (int t = 0; t <= 1440; ++t) {
            auto stA = t;
            auto enA = (t + 720) % 1440;
            if (enA == 0) {
                enA = 1440;
            }
            int ok = 0;
            for (int i = 1; i <= n; ++i) {
                if (a[i].first < stA && stA < a[i].second) {
                    ok = 1;
                }
            }
            for (int i = 1; i <= n; ++i) {
                if (a[i].first < enA && enA < a[i].second) {
                    ok = 1;
                }
            }
            for (int i = 1; i <= m; ++i) {
                if (b[i].first < stA && stA < b[i].second) {
                    ok = 1;
                }
            }
            for (int i = 1; i <= m; ++i)
                if (b[i].first < enA && enA < b[i].second) {
                    { ok = 1; }
                }
            if (ok)
                continue;

            int xA = 0, yB = 0;
            for (int i = 1; i <= n; ++i) {
                if (t <= 720) {
                    if (stA <= a[i].first && a[i].second <= enA) {
                        xA++;
                    }
                } else {
                    if (stA <= a[i].first && a[i].second <= 1440) {
                        xA++;
                    }
                    if (0 <= a[i].first && a[i].second <= enA) {
                        xA++;
                    }
                }
            }
            for (int i = 1; i <= m; ++i) {
                if (t <= 720) {
                    if (stA <= b[i].first && b[i].second <= enA) {
                        yB++;
                    }
                } else {
                    if (stA <= b[i].first && b[i].second <= 1440) {
                        yB++;
                    }
                    if (0 <= b[i].first && b[i].second <= enA) {
                        yB++;
                    }
                }
            }
            int tmp = yB * 2 + (n - xA) * 2;
            ans = std::min(ans, tmp);
        }

        std::cout << "Case #" << ti << ": " << ans + 2 << std::endl;
    }
}
