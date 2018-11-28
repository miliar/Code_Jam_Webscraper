#include <iostream>
#include <vector>
#include <bitset>
#include <iterator>
#include <algorithm>
#include <string>
#include <array>
#include "brick-query"

using namespace std;
using namespace brick::query;

struct Stall {
    Stall( const Stall & ) = default;
    Stall( bool e, int l, int r ) : empty(e), L(l), R(r) {}

    bool empty;
    int L;
    int R;
};

using Stalls = vector< Stall >;

void place( Stalls & stalls, int pos ) {
    stalls[ pos ].empty = false;
    for ( int i = pos - 1; i > 0; --i ) {
        if ( !stalls[i].empty )
            break;
        stalls[i].R = pos - i - 1;
    }
    for ( int i = pos + 1; i < stalls.size() - 1; ++i ) {
        if ( !stalls[i].empty )
            break;
        stalls[i].L = i - pos - 1;
    }
    stalls[ pos ].L = 0;
    stalls[ pos ].R = 0;
}

auto minv = [] ( auto & v ) {
    return query(v).map( [] ( auto & s ) { return std::min( s.L, s.R );} ).max();
};

auto maxv = [] ( auto & v ) {
    return query( v ).map( [] ( auto & s ) { return std::max( s.L, s.R ); } ).max();
};

pair< int, int > iteration( Stalls & stalls ) {
    Stalls empty;
    for (auto & s : stalls)
        if (s.empty)
            empty.push_back(s);
    int min = minv(empty);
    vector< int > positions;
    for ( int i = 0; i < stalls.size(); ++i ) {
        auto& s = stalls[i];
        if ( s.empty && std::min( s.L, s.R ) == min )
            positions.push_back(i);
    }

    Stalls potential;
    for ( int p : positions )
        potential.push_back( stalls[p] );
    int max = maxv( potential );
    int pos;
    if ( positions.size() == 1 ) {
        pos = positions[0];
    } else {
        for ( int i = 0; i < positions.size(); ++i ) {
            auto s = stalls[ positions[i] ];
            if ( std::max( s.L, s.R ) == max ) {
                pos = positions[i];
                break;
            }
        }
    }
    place( stalls, pos );
    /*for ( auto & s : stalls )
        cout << s.empty;
    cout << endl;
    for ( auto & s : stalls )
        cout << s.L;
    cout << endl;
    for ( auto & s : stalls )
        cout << s.R;
    cout << endl;
    cout << min << " " << max << endl;
    cout << endl;*/
    return { min, max };
}

int main() {
    int rows;
    cin >> rows;
    cin.ignore();

    for ( int i = 0; i < rows; ++i ) {
        int N, K;
        cin >> N;
        cin >> K;
        Stalls stalls;
        stalls.reserve(N + 2);

        stalls.emplace_back( false, 0, 0 );
        for ( int k = 1; k <= N; ++k )
            stalls.emplace_back( true, k - 1, N - k );
        stalls.emplace_back( false, 0, 0 );
        pair< int, int > p;
        for ( int k = 0; k < K; ++k ) {
            p = iteration( stalls );
        }
        cout << "Case #" << i + 1 << ": " << p.second << " " << p.first << endl;
    }
}
