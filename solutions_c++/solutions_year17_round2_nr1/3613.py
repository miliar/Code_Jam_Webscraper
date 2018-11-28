#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t) {
        double D, N;
        cin >> D >> N;
        
        double m = -1;
        for( int i = 0; i < N; ++i ) {
            double K, S;
            cin >> K >> S;
            double x = ( D - K ) / S;
            if( x > m ) m = x;
        }

        cout << "Case #" << t << ": ";
        
        cout << fixed << setprecision( 6 ) << ( D / m );

        cout << "\n";
    }

    return 0;
}