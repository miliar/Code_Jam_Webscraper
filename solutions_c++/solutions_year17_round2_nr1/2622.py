#include <iostream>
#include <iomanip>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;
using ll = long long;

int main()
{
    int T;
    cin >> T;

    for( int t = 1; t <= T; ++t )
    {
        cout << "Case #" << t << ": ";

        ll D, N;
        cin >> D >> N;

        double tmax = 0;
        for (int i = 1; i <= N; ++i) {
            ll K, S;
            cin >> K >> S;
            
            double ti = (double)(D-K)/(double)S;
            tmax = max(tmax, ti);
        }

        double S = (double)D/tmax;
        cout << setprecision(20) << S;

        cout << endl;
    }

    return 0;
}
