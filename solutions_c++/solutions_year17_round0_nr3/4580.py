#include <iostream>
#include <cstdint>

using namespace std;

uint64_t maxpow2(uint64_t x)
{
    uint64_t r = 0;

    while(x >= ((uint64_t)1 << r)) {
        ++r;
    }

    return r - 1;
}

static inline uint64_t pow2(uint64_t x)
{
    return (uint64_t)1 << x;
}

void solve(ostream& os, istream& is)
{
    uint64_t k, n;
    is >> n >> k;

    uint64_t slots_at_level = (uint64_t)1 << 63;

    while(slots_at_level > k) {
        slots_at_level = slots_at_level >> 1;
    }
    
    uint64_t stalls_left_at_level = n - (slots_at_level - 1);

    uint64_t spare_stalls = stalls_left_at_level % slots_at_level;
    uint64_t stalls_per_newcommer = stalls_left_at_level / slots_at_level;

    // newcommer takes one stall
    --stalls_per_newcommer;

    // any spare stall to add?
    if(k - (slots_at_level - 1) <= spare_stalls) {
        ++stalls_per_newcommer;
    }

    uint64_t min = stalls_per_newcommer / 2;
    uint64_t max = min;
    if(stalls_per_newcommer & 1) {
        ++max;
    }

    os << max << " " << min;
}

int main()
{
    int C;

    cin >> C;

    for(int c = 0; c < C; ++c) {
        cout << "Case #" << c + 1 << ": ";
        solve(cout, cin);
        cout << endl;
    }

    return 0;
}

