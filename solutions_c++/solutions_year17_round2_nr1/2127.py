#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>

using namespace std;

vector< pair< long long, long long > > hor;

bool check( long double speed, int N )
{
    long double time = N / speed;

    for ( int i = 0; i < hor.size( ); ++i )
    {
        long double time_h = ( ( long double )( N - hor[ i ].first ) ) / hor[ i ].second;
        if ( time_h > time )
        {
            return false;
        }
    }
    return true;
}

long double bin_search( int N )
{
    long double left = 0.00000000;
    long double right = 1.0e+25;

    int iteration = 0;


    while ( left <= right )
    {
        iteration++;
        long double  mid = ( left + right ) / 2;
        if ( check( mid, N ) )
        {
            left = mid;
        }
        else
        {
            right = mid;
        }

        if ( iteration >= 150 )
        {
            return mid;
        }
    }

    return ( left + right ) / 2;

}

int main( )
{

    freopen( "in.txt", "r", stdin );
    freopen( "out.txt", "w", stdout );



    int T;
    cin >> T;
    for ( int t = 0; t < T; ++t )
    {
        int d, n;
        cin >> d >> n;


        hor.resize( n );

        for ( int i = 0; i < n; ++i )
        {
            cin >> hor[ i ].first >> hor[ i ].second;
        }


        auto ans = bin_search( d );

        printf( "Case #%d: %.*lf\n", t + 1, 12, ans );

    }

    return 0;
}