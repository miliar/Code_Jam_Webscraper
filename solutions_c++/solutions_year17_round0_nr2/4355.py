#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

typedef unsigned long long llu;

int n;
string S;

string patch( string A, int i ) {
    string B = A;
    for( int j = i; j < n; j++ ) {
        B += '9';
    }
    return B;
}

bool valid( string A ) {
    for( int i = 1; i < A.length(); i++ ) {
        if( A[ i ] < A[ i - 1 ] ) return false;
    }
    return true;
}

int main( void ) {
    int T;
    scanf("%d", &T );
    for( int t = 1; t <= T; t++ ) {
        cin >> S;
        n = ( int ) S.length();
        string current, ans;
        if( valid( S ) ) ans = S;
        current += ( char )( S[ 0 ] );
        current[ 0 ]--;
        ans = max( ans, patch( current, 1 ) );
        for( int i = 1; i < n; i++ ) {
            current[ i - 1 ]++;
            current += S[ i ] - 1;
            if( current[ i ] + 1 < current[ i - 1 ] ) break;
            if( current[ i ] < current[ i - 1 ] ) continue;
            if( patch( current, i + 1 ) > ans ) {
                ans = patch( current, i + 1 );
            }
        }
        while( *( ans.begin() ) == '0' ) ans.erase( ans.begin() );
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
