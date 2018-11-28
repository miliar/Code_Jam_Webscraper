
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

int ceilfrac(int a, int b)
{
    int q = a/b;
    if ( a%b != 0 )
        ++q;
    return q;
}

void solve()
{
    int seats, customers, tickets;
    std::cin >> seats >> customers >> tickets;
    std::vector< std::pair<int,int> > dat;
    for ( int i = 0 ; i < tickets ; ++i ) {
        int a,b;
        std::cin >> a >> b;
        --a;
        --b;
        dat.emplace_back( a , b );
    }
    std::sort( dat.begin() , dat.end() );

    int rides = 0;
    // rides >= max # tickets bought by any one dude.
    std::vector< std::vector<int> > perCustomer( customers );
    for ( int i = 0 ; i < dat.size() ; ++i )
        perCustomer[ dat[i].second ].push_back( dat[i].first );

    for ( int i = 0 ; i < customers ; ++i )
        rides = std::max( rides , (int)perCustomer[i].size() );

    std::vector< std::vector<int> > perSeat( seats );
    for ( int i = 0 ; i < dat.size() ; ++i )
        perSeat[ dat[i].first ].push_back( dat[i].second );

    // rides >= max ceil of (# for seats 123..k) / k.
    int running = 0;
    for ( int k = 1 ; k <= seats ; ++k ) {
        running += perSeat[k-1].size();
        int curr = ceilfrac( running , k );
        rides = std::max( rides , curr );
    }

    // how many promotions are necessary to get here?
    int moves = 0;
    
    // start from the back.
    // if I see more tickets at seat K than can fit, I need to promote some.
    for ( int k = seats-1 ; k >= 0 ; --k ) {
        if ( perSeat[ k ].size() > rides )
            moves += perSeat[k].size() - rides;
    }
    
    std::cout << rides << ' ' << moves << '\n';
}

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {
        std::cout << "Case #" << testID << ": ";
        solve();
    }

    return 0;
}
