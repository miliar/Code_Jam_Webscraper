
#include <iostream>
#include <map>
#include <utility>

typedef long long ll;

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {
        ll N,K;
        std::cin >> N >> K;

        std::map<ll,ll> slots;
        slots[ N ] = 1;
        while ( slots.rbegin()->second < K ) {
            auto it = slots.end();
            --it;
            std::pair<ll,ll> curr = *it;
            slots.erase( it );
            K -= curr.second;
            slots[ curr.first/2 ] += curr.second;
            slots[ (curr.first-1)/2 ] += curr.second;
        }
        std::pair<ll,ll> curr = *slots.rbegin();
        ll final = curr.first;
        std::cout << "Case #" << testID << ": ";
        std::cout << final/2 << ' ';
        std::cout << (final-1)/2 << '\n';
    }

    return 0;
}
