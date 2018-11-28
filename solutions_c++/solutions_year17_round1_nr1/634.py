#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cassert>
#include <cstring>
#include <tuple>
#include <set>
#include <map>
#include <utility>

using ll = long long;
using pii = std::pair<int,int>;

const int MAX = 33;
int R, C;
std::string cake[MAX];
std::string orig[MAX];

void solve()
{
    std::set<char> seen;
    for (int r = 0; r < R; ++r)
        orig[r] = cake[r];
    bool changed = true;
    int pr = 0, pc = 0;
    while (changed) {
        changed = false;
        for (int r = pr; r < R; ++r)
            for (int c = pc; c < C; ++c)
                if (cake[r][c] != '?') {
                    if (seen.count(cake[r][c]))
                        continue;
                    char tmp = cake[r][c];
                    seen.insert(tmp);
                    cake[r][c] = '?';
                    int y = c+1;
                    while (y < C && cake[r][y] == '?') 
                        ++y;
                    int x = r+1;
                    bool cont = true;
                    while (x < R && cont) {
                        for (int c1 = 0; c1 < y; ++c1)
                            if (cake[x][c1] != '?' && !seen.count(cake[x][c1]))
                                cont = false;
                        if (cont)
                            ++x;
                    }
                    for (int i = pr; i < x; ++i)
                        for (int j = pc; j < y; ++j)
                            if (cake[i][j] == '?') {
                                cake[i][j] = tmp;
                                changed = true;
                            }
                    if (y == C) {
                        pr = r+1;
                        pc = 0;
                    } else {
                        pc = y;
                    }
                    goto out;
                }
out:
        ;
        /* for (int r = 0; r < R; ++r) */
        /*     std::cout << cake[r] << std::endl; */
    }
    bool good = true;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (cake[i][j] == '?' || 
                    (orig[i][j] != '?' && cake[i][j] != orig[i][j]))
                good = false;

    if (good) {
        for (int r = 0; r < R; ++r)
            std::cout << cake[r] << std::endl;
    } else {
        assert(false);
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> R >> C;
        for (int r = 0; r < R; ++r)
            std::cin >> cake[r];

        std::cout << "Case #" << cs << ":" << std::endl;
        solve();
    }
}



