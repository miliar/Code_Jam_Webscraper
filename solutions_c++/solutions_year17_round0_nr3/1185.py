//
// Created by manojrk on 4/8/17.
//

#include <iostream>
#include <map>

#define ll long long int

void addTo(std::map<ll, ll, std::greater<ll>> &map, ll index, ll value) {
    auto it = map.find(index);
    if (it != map.end()) {
        it->second += value;
    } else {
        map[index] = value;
    }
}

void get_stalls() {
    ll n, k;
    std::cin >> n >> k;
    std::map<ll, ll, std::greater<ll>> ranges;
    ranges[n] = 1;
    while (true) {
        auto biggest = ranges.begin();
        ll size = biggest->first;
        ll count = biggest->second;
        ll ls = size / 2;
        ll rs = size - ls - 1;
        if (count >= k) {
            std::cout << std::max(ls, rs) << ' ' << std::min(ls, rs);
            break;
        }
        ranges.erase(biggest);
        addTo(ranges, ls, count);
        addTo(ranges, rs, count);
        k -= count;
    }
}

int main() {
    int tc;
    std::cin >> tc;
    for (int i = 1; i <= tc; ++i) {
        std::cout << "Case #" << i << ": ";
        get_stalls();
        std::cout << std::endl;
    }
    return 0;
}
