#include <iostream>
#include <string>

using namespace std;

int get_solution( string pancakes, const int K ) {
    const int length = pancakes.length();
    
    int flips = 0;
    for( int i = 0; i < length; ++i ) {
        if( pancakes[ i ] == '+' ) continue;
        
        if( i + K > length ) {
            for( int z = 0; z < K; ++z ) {
                if( pancakes[ i ] == '-' ) return -1;
            }
        }

        for( int z = 0; z < K; ++z ) {
            pancakes[ i + z ] = pancakes[ i + z ] == '+' ? '-' : '+'; 
        }
        ++flips;
    }

    return flips;
}

int normalize( const int element ) {
    return element == -1 ? 1 << 30 : element;
}

int main() {

    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t ) {
        string pancakes;
        int K;
        cin >> pancakes >> K;

        const int a = get_solution( pancakes, K );

        reverse( pancakes.begin(), pancakes.end() );
        const int b = get_solution( pancakes, K );

        cout << "Case #" << t << ": ";

        if( a == -1 && b == -1 ) cout << "IMPOSSIBLE";
        else cout << min( normalize( a ), normalize( b ) );

        cout << "\n";
    }

    return 0;
}