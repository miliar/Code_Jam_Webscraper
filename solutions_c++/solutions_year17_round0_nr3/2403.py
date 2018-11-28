#include <iostream>
#include <utility>

typedef unsigned long long ullong;

using namespace std;

std::pair<ullong,ullong> solve (ullong N, ullong K) {
    std::pair<ullong,ullong> z(0,0);
    if (N==K)
        return z;

    // cd*(9)          => 2*cd*(4)
    // cd*(8)          =>   cd*(4) + cd*(3)
    // cd*(8) + cm*(7) =>   cd*(4) + cd*(3) + 2*cm*(3) ; sd'=4
    // cd*(7) + cm*(6) => 2*cd*(3) + cm*(3) +   cm*(2) ; sd'=3

    ullong sd = N;      // size  duzy
    ullong cd = 1;      // count duzy
    ullong cm = 0;      // count maly

    while (1 <= K) {
        // cerr << "=== K: " << K << " sd=" << sd << " cd=" << cd << " cm=" << cm << endl;

        const ullong odd = (sd % 2);
        const ullong sd2 = (sd / 2);

        if (K <= cd) {
            z.first  = sd2;
            z.second = sd2 - (odd ? 0 : 1);
            break;
        } else if (K <= cd+cm) {
            z.first  = sd2 - (odd ? 0 : 1);
            z.second = sd2 - 1;
            break;
        } else {
            const ullong cd2 = (odd ? (2*cd+cm) : cd);
            const ullong cm2 = (odd ? cm : (cd+2*cm)); 
            
            K -= cd;
            K -= cm;
    
            sd = sd2;
            cd = cd2;
            cm = cm2;
        }
    }

    return z; 
}

int main() {
    int T=0;
    cin >> T;

    for (int i=0; i<T; ++i) {
        ullong N=0;
        ullong K=0;

        cin >> N;
        cin >> K;

        std::pair<ullong,ullong> res(solve(N,K));
        cout << "Case #" << (1+i) << ": " << res.first << " " << res.second << endl;
    }

    return 0;
}
