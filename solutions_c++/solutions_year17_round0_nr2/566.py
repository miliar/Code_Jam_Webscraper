#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cassert>

using ll = long long;

ll N;

bool tidy(ll n)
{
    ll cur = n % 10; n /= 10;
    while (n) {
        if (n % 10 > cur) 
            return false;
        cur = n % 10;
        n /= 10;
    }
    return true;
}

ll small()
{
    for (int i = N; ; --i)
        if (tidy(i))
            return i;
    assert(false);
}


ll solve()
{
    ll cur = N;
    while (!tidy(cur)) {
        ll rem = cur % 10, tmp = cur / 10, mult = 10;
        while (tmp) {
            if (tmp % 10 > rem) {
                cur = cur / mult * mult - 1;
                break;
            }
            mult *= 10;
            rem = tmp % 10;
            tmp /= 10;
        }
    }
    return cur;
}

int main() {
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N;

        ll ans = solve();
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }
}

