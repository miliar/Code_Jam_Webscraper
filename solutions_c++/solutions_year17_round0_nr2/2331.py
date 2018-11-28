#include <iostream>
#include <vector>
#include <algorithm>

typedef unsigned long long ullong;

const int MaxP = 18;
std::vector<ullong> pow10;

using namespace std;

ullong solve(ullong N) {
    short  d = 9;       // previous digit
    ullong p = N;       // result prefix
    short  s = 0;       // result suffix (10^s-1) (czyli tyle 9)
    int    i = 0;

    for (; (1<=N); ++i) {
        short r = N % 10;
        // cerr << "i=" << i << " N=" << N << " r=" << r << " d=" << d << " p=" << p << " s=" << s << endl;
        
        if (d < r) {
            d = r - 1;
            s = i;
            p = N - 1;
        } else {
            d = r;
        }

        N /= 10;        
    }

    return (p * pow10[s] + pow10[s] - 1);
}

void init() {
    ullong p=1;
    for (int i=0; i<=1+MaxP; ++i) {
        pow10.push_back(p);
        p *= 10;
    }
}

int main() {
    init();

    int T=0;
    cin >> T;

    for (int i=0; i<T; ++i) {
        ullong N=0;
        cin >> N;
        cout << "Case #" << (1+i) << ": " << solve(N) << endl;
    }

    return 0;
}
