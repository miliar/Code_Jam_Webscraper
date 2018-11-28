#include <iostream>
#include <string>
#include <queue>

using namespace std;

typedef pair<long, long> pii;

int T;
long long n, k;
long long a, b;
long long newa, newb;
long long c1, c2;
long long newc1, newc2;

pii split(long long n) {
    return make_pair(n >> 1, (n >> 1) - !(n & 1));
}

int main() {
    cin >>T;
    for (int i = 1; i <= T; i++) {
        cin >>n >>k;
        long long p = 1;
        c1 = 1; c2 = 0; a = n; b = n;
        while(k > p) {
            newa = split(a).first;
            newb = split(a).second;
            if (newa == newb) {
                newc1 = (c1 << 1) + c2;
                newc2 = c2;
            }
            else {
                newc1 = c1;
                newc2 = (c2 << 1) + c1;
            }
            a = newa;
            b = split(b).second;
            c1 = newc1; c2 = newc2;
            k -= p;
            p <<= 1;
            // printf("a = %lld with count %lld\n", a, c1);
            // printf("b = %lld with count %lld\n", b, c2);
        }
        if (k <= c1) {
            newa = split(a).first;
            newb = split(a).second;
        } else {
            newa = split(b).first;
            newb = split(b).second;
        }
        cout <<"Case #" <<i <<": " <<newa <<' ' <<newb <<endl;
    }
    return 0;
}
