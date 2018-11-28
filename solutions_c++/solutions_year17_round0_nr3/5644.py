#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        long N, K;
        cin >> N >> K;
        int n = floor(log2(K + 1));
        long k = (1 << n) - 1;
        long m = K - k;
        long small = floor((long double) (N - k) / (1 << n)), large = ceil((long double) (N - k) / (1 << n));
        long clarge = (N - k) - small * (1 << n);

        if (m == 0) {
            if(clarge != 0)
                cout << "Case #" << i << ": " << large << " "  << small << endl;
            else
                cout << "Case #" << i << ": " << small << " "  << small << endl;
        }
        else {
            long p;
            if(m <= clarge)
                p = large;
            else
                p = small;

            if(p % 2 == 0)
                cout << "Case #" << i << ": " << p / 2 << " " << p / 2 - 1 << endl;
            else
                cout << "Case #" << i << ": " << p / 2 << " " << p / 2 << endl;

        }
    }
}