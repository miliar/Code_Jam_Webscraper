#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, k, ans;
string s, tmp;

bool check( string s ) {

    for ( int i = 0; i < s.size(); ++i ) {
        if ( s[i] != '+' ) {
            return ( false );
        }
    }

    return ( true );

}

int bfs( string start, int k ) {

    queue <string> q;
    set <string> s;
    map <string,int> m;

    q.push( start );
    s.insert( start );

    m[ start ] = 0;

    if ( check( start ) ) {
        return ( 0 );
    }

    while ( !q.empty() ) {

        string top = q.front();
        q.pop();

        for ( int i = 0; i < top.size()-k+1; ++i ) {
            //---+-++-
            //cout << top[i] << "|";

            //flip next k
            tmp = top;
            for ( int j = 0; j < k; ++j ) {
                if ( tmp[i+j] == '+' ) {
                    tmp[i+j] = '-';
                }else {
                    tmp[i+j] = '+';
                }
            }

            if ( s.find( tmp ) == s.end() ) {
                q.push( tmp );
                s.insert( tmp );
                m[ tmp ] = m[ top ] + 1;
                if ( check( tmp ) ) {
                    return ( m[tmp] );
                }
            }

        }

    }

    return ( -1 );

}

int main( ) {

    cin >> n;

    for ( int i = 1; i <= n; ++i ) {

        cin >> s >> k;

        ans = bfs( s, k );

        printf( "Case #%d: ", i );

        if ( ans == -1 ) {
            printf( "IMPOSSIBLE" );
        }else {
            printf( "%d", ans );
        }

        printf( "\n" );

    }

    return 0;

}
