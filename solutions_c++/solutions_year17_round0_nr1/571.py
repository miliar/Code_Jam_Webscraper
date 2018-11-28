#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <tuple>
#include <set>
#include <map>

using ll = long long;

std::string S;
int K;

void flip(int x)
{
    for (int i = x; i < x+K; ++i)
        S[i] = S[i] == '-' ? '+' : '-';
}

int solve()
{
    int k = 0;
    for (int i = 0; i <= S.size() - K; ++i) {
        if (S[i] == '+') continue;
        flip(i);
        ++k;
    }
    return S.find('-') == std::string::npos ? k : -1;
}

int main() {
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> S >> K;

        int sol = solve();
        auto ans = sol == -1 ? "IMPOSSIBLE" : std::to_string(sol);
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }
}



