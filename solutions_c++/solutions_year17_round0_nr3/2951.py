#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int T;

void read() {
    cin >> T;
}

//2 ^ (log nr)
unsigned long long logPow(unsigned long long nr) {
    if (nr == 0) {
        return 1;
    }

    unsigned long long aux = (unsigned long long)(1) << 63;

    while (!(aux & nr)) {
        aux >>= 1;
    }

    return aux;
}

unsigned long long getMax(unsigned long long k, unsigned long long n) {
    if (k == 0) {
        return n;
    }

    //never happens
    if (k == n) {
        return 0;
    }

    unsigned long long pow = logPow(k + 1);
    //k + 1 nu e putere a lui 2
    if ((k + 1) & k) {
        return (n - 1) / pow;
    }
    return n / pow;
}

class Comparator {
public:
    bool operator()(const unsigned long long& x, const unsigned long long& y) {
        return x > y;
    }
};

typedef map<unsigned long long, unsigned long long, Comparator> Map;

void solve() {
    unsigned long long n, k, curr;
    Map a, b;

    for (int i = 0; i < T; ++i) {
        cin >> n >> k;
        a.erase(a.begin(), a.end());
        a[n] = 1;
        while (k) {
            b.erase(b.begin(), b.end());
            for (auto it : a) {
                curr = it.first;
                if (k < 1 + it.second) {
                    k = 0;
                    break;
                } else {
                    k -= it.second;
                }
                //merge pt ca se creeaza cand apelez []
                --curr;
                if (curr % 2) {
                    b[curr / 2] += it.second;
                    b[(curr + 1)/ 2] += it.second;
                } else {
                    b[curr / 2] += 2 * it.second;
                }
            }
            a = Map(b);
        }
        cout << "Case #" << i + 1 << ": ";
        cout << curr / 2 << " " << (curr - 1) / 2;
        cout << endl;
    }
}

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    read();
    solve();
    return 0;
}
