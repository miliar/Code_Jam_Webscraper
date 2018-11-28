#include <algorithm>
#include <cassert>
#include <cstring>
#include <deque>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

int main() {
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/in.txt", "r", stdin);
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/out.txt", "w", stdout);

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        std::string s;
        std::cin >> s;

        int n = s.size();
        std::vector<int> digs(n);
        for (int i = 0; i < n; ++i) {
            digs[i] = s[i] - '0';
        }
        for (int i = 0; i < n; ++i) {
            bool ok = true;
            for (int j = i + 1; j < n; ++j) {
                if (digs[j] > digs[i]) {
                    break;
                }
                if (digs[j] == digs[i]) {
                    continue;
                }
                ok = false;
                break;
            }
            if (!ok) {
                --digs[i];
                for (int j = i + 1; j < n; ++j) {
                    digs[j] = 9;
                }
            }
        }

        std::size_t i = 0;
        while (digs[i] == 0) {
            ++i;
        }

        std::cout << "Case #" << ti << ": ";
        while (i < digs.size()) {
            std::cout << digs[i++];
        }
        std::cout << std::endl;
    }
}