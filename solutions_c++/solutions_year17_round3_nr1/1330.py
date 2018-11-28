#include <bits/stdc++.h>

using namespace std;

ifstream in("pancakes.in");
ofstream out("pancakes.out");

typedef long long I64;
const double PI = 3.14159265359;
const int NMAX  = 1000;

vector< pair<I64, I64> > v;
I64 d[NMAX+5][NMAX+5];
int T, N, K;

void QUERY() {
    memset( d, 0, sizeof(d) );
    v.clear();

    in >> N >> K;
    for( int i = 1;  i <= N;  ++i ) {
        I64 r, h;
        in >> r >> h;
        v.push_back( {r,h} );
    }
    sort( v.begin(), v.end() );
    reverse( v.begin(), v.end() );
    for( int i = 0;  i < N;  ++i ) {
        d[i][1] = v[i].first * v[i].first + 2*v[i].first * v[i].second;
        if( i > 0 ) d[i][1] = max( d[i-1][1], d[i][1] );
        for( int j = 2;  j <= K;  ++j ) {
            /// aici adaug doar peretii
            if( i == 0 ) continue;
            I64 cost = d[i-1][j-1] + 2*v[i].first * v[i].second;
            d[i][j] = max( d[i-1][j], cost );
        }
    }
    out << setprecision(9) << fixed << PI * d[N-1][K];
}

int main()
{
    in >> T;
    for( int t = 1;  t <= T;  ++t ) {
        out << "Case #" << t << ": ";
        QUERY();
        out << '\n';
    }
    return 0;
}
