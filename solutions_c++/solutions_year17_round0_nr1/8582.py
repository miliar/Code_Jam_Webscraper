#include <iostream>
#include <vector>
#include <bitset>
#include <iterator>
#include <algorithm>
#include <string>
#include "brick-query"

using namespace std;
using namespace brick::query;

using Bits = std::vector<bool>;

auto Happy = [] ( const Bits & bits ) {
    return query(bits).all( [] ( auto b ) { return b; } );
};

auto Sad = [] ( const Bits & bits ) {
    return query(bits).none( [] ( auto b ) { return b; } );
};

void flip( Bits::iterator && from, const int mask_size ) {
    for ( auto it = from; it != from + mask_size; ++it )
        (*it) = !(*it);
}

int flips( Bits & bits, const int mask_size ) {
    if ( Happy( bits ) )
        return 0;

    int count = 0;
    for ( int i = 0; i < bits.size() - mask_size + 1; ++i ) {
        if ( !bits[i] ) {
            flip( bits.begin() + i, mask_size );
            ++count;
        }
    }
    if ( !Happy( bits ) )
        return -1;
    else
        return count;
}

int main() {
    int rows;
    cin >> rows;
    cin.ignore();

    for ( int i = 0; i < rows; ++i ) {
        string in;
        size_t mask_size;
        getline(cin, in, ' ');
        cin >> mask_size;
        cin.ignore();

        Bits row;
        transform( in.begin(), in.end(), back_inserter( row ),
        [] ( char c ) { return c == '+'; } );

        auto f = flips( row, mask_size );
        if ( f == -1 )
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i + 1 << ": " << f << endl;
    }
}
