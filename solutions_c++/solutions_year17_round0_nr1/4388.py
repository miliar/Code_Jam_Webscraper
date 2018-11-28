#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

string A;

void change( int i, int K ) {
    for( int j = i; j <= i + K - 1; j++ ) {
        if( A[ j ] == '+' ) A[ j ] = '-';
        else A[ j ] = '+';
    }
}

int main( void ) {
    int T;
    scanf("%d", &T );
    for( int t = 1; t <= T; t++ ) {
        int K, N, ans = 0;
        cin >> A >> K;
        N = ( int )A.length();
        for( int i = 0; i < N - K + 1; i++ ) {
            if( A[ i ] == '-' ) {
                change( i, K );
                ans++;
            }
        }
        bool status = true;
        for( int i = N - K + 1; i < N; i++ ) {
            if( A[ i ] == '-' ) status = false;
        }
        if( status ) {
            printf("Case #%d: %d\n", t, ans );
        } else {
            printf("Case #%d: IMPOSSIBLE\n", t );
        }
    }
    return 0;
}
