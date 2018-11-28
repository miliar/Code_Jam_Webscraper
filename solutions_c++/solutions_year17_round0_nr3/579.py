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

ll N, K;
bool filled[1111];

std::pair<int,int> brute()
{
    memset(filled, false, sizeof(filled));
    filled[0] = filled[N+1] = true;
    int hi, lo;
    for (int i = 0; i < K; ++i) {
        std::set<std::tuple<int,int,int>> hold; 
        for (int j = 1; j <= N; ++j) {
            if (filled[j]) continue;
            int l = j-1, r = j+1;
            while (!filled[l]) --l;
            while (!filled[r]) ++r;
            hold.emplace(-std::min(j-l,r-j), -std::max(j-l,r-j), j);
        }
        int pos;
        std::tie(lo, hi, pos) = *hold.begin();
        filled[pos] = true;
    }
    return {-hi-1,-lo-1};
}

std::pair<ll,ll> solve()
{
    std::map<ll,ll> left;
    left[N] = 1;
    ll sz, cnt;
    while (true) {
        std::tie(sz, cnt) = *left.rbegin();
        if (cnt >= K) {
            return {sz/2, (sz-1)/2};
        }
        K -= cnt;
        left[(sz-1)/2] += cnt;
        left[sz/2] += cnt;
        left.erase(left.find(sz));
    }
}

int main() {
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N >> K;

        auto ans = solve();
        std::cout << "Case #" << cs << ": " << ans.first << ' ' << ans.second << std::endl;
    }
}


