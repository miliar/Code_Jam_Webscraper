#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>

using namespace std;


map<char, int> used;


char firts;

string resolve( vector< pair< int, char > > h )
{
    char prev = 'Z';
    firts = 'Z';

    string answ;
    used.clear( );


    struct cmp
    {

        bool operator( ) ( pair< int, char > left, pair< int, char > right )
        {
            if ( left.first != right.first )
            {
                return left.first > right.first;
            }

            if( left.second != right.second )
            {
                return left.second == firts;
            }
            return false;
        }
    };

    while ( true )
    {

        sort( h.begin( ), h.end( ), cmp( ) );

        bool zero = true;
        for ( int i = 0; i < h.size( ); ++i )
        {
            if ( h[ i ].first > 0 )
            {
                zero = false;
                break;
            }
        }
        if ( zero )
        {
            if ( answ.front( ) == answ.back( ) )
            {
                return "IMPOSSIBLE";
            }
            else
            {
                return answ;
            }
        }

        bool update = false;
        for ( auto it = h.begin( ); it != h.end( ); ++it )
        {

            if ( it->first > 0 && prev != it->second )
            {
                prev = it->second;
                --it->first;
                answ.push_back( prev );
                used[ prev ] = answ.size( );
                update = true;
                break;
            }
        }
        if ( !update )
        {
            return "IMPOSSIBLE";
        }
        firts = answ[ 0 ];
    }
}

int main( )
{

    freopen( "in.txt", "r", stdin );
    freopen( "out.txt", "w", stdout );



    int T;
    cin >> T;
    for ( int t = 0; t < T; ++t )
    {
        vector< pair< int, char > > h;
        h.resize( 6 );

        int n; cin >> n;

        for ( int i = 0; i < 6; ++i )
        {
            cin >> h[ i ].first;
        }

        h[ 0 ].second = 'R';
        h[ 1 ].second = 'O';
        h[ 2 ].second = 'Y';
        h[ 3 ].second = 'G';
        h[ 4 ].second = 'B';
        h[ 5 ].second = 'V';

        //vector< char > st = { 'N', 'R', 'O', 'Y', 'G', 'B', 'V' };
        //for ( int i = 0; i < st.size( ); ++i )
        //{
        //    for( int j = 0; j < h.size( ); ++j )
        //}


        auto answ = resolve( h );

        printf( "Case #%d: %s\n", t + 1, answ.c_str( ) );

    }

    return 0;
}