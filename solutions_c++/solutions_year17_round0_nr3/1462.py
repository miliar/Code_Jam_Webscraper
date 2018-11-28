#define LL long long int
#include <iostream>
using namespace std;

pair<LL, LL> calc(LL w) {
    if (w&1) return make_pair(w/2, w/2);
    else return make_pair(w/2, w/2-1);
}

pair<LL, LL> maxminl(LL n, LL k) {
    if (n == k) return make_pair(0,0);

    LL d = 1;
    while (k > 0) {
        LL w1 = n/d, w2 = (n%d==0 ? w1 : w1+1);
        LL n2 = n - d*w1, n1 = min(d - n2, n-n2);

        if (k <= n2) return calc(w2);
        k -= n2;
        if (k <= n1) return calc(w1);
        k -= n1;
        
        n -= n1 + n2;
        d <<= 1;
    }
}

int main() {
    int t;
    cin >> t;
    LL n, k;
    for (int c = 1; c <= t; c++) {
        cin >> n >> k;
        pair<LL, LL> r = maxminl(n,k);
        cout << "Case #" << c << ": " << r.first << " " << r.second << endl;    
    }
}
