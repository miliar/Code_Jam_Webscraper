#include <algorithm>
#include <cassert>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

const int inf = 1e9;

std::pair<int, int> h[1010];

int main() {
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/in.txt", "r", stdin);
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/out.txt", "w", stdout);

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int d, n;
        std::cin >> d >> n;

        for (int i = 1; i <= n; ++i) {
            std::cin >> h[i].first >> h[i].second;
        }
        std::sort(h + 1, h + n + 1);

        double t = 0;
        for (int i = 1; i <= n; ++i) {
            t = std::max(t, (double)(d - h[i].first) / h[i].second);
        }

        double answer = d / t;
        std::cout << "Case #" << ti << ": " << std::setprecision(10) << std::fixed << answer << std::endl;
    }
}