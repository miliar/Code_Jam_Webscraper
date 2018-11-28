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

int c[6];

int main() {
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/in.txt", "r", stdin);
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/out.txt", "w", stdout);

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int n;
        std::cin >> n;

        // r, o, y, g, b, v
        for (int i = 0; i < 6; ++i) {
            std::cin >> c[i];
        }

        std::cout << "Case #" << ti << ": ";
        auto r = c[0];
        auto y = c[2];
        auto b = c[4];
        if (r > y + b || y > b + r || b > r + y) {
            std::cout << "IMPOSSIBLE";
        } else {
            std::vector<int> id = { 0, 1, 2, 3, 4, 5 };
            std::sort(id.begin(), id.end(), [](int i, int j) {
                return c[i] > c[j];
            });

            std::vector<int> orders;
            int x = id[0];
            int y = id[1];
            int z = id[2];
            for (int i = 0; i < c[x]; ++i) {
                orders.push_back(x);
                if (i < c[y]) {
                    orders.push_back(y);                        
                }
                if (i >= c[x] - c[z]) {
                    orders.push_back(z);
                }
            }
            const std::string k = "ROYGBV";
            for (int i = 0; i < n; ++i) {                
                std::cout << k[orders[i]];
            }
        }
        std::cout << std::endl;
    }
}