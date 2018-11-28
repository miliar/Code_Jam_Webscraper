#include <iostream>

using namespace std;

typedef long long int lli;

lli firstPowerOfTwoBelow(lli x) {
    lli out = 0, y = 1;
    while ((y << 1) <= x) {
        y <<= 1;
        out++;
    }
    return out;
}

int main() {
	int t; cin >> t;
	for (int c = 1; c <= t; c++) {
	    lli x, k;
	    cin >> x >> k;

	    lli y = 1;
	    lli p2 = firstPowerOfTwoBelow(k);
	    lli val = x, ct = 1, m1 = 0;
	    for (int i = 0; i < p2; i++) {
            if (val % 2 == 0) {
                val >>= 1;
                m1 <<= 1;
                m1 += ct;
            } else {
                val >>= 1;
                ct <<= 1;
                ct += m1;
            }
            y <<= 1;
	    }

	    lli outnum;
	    if (y + ct > k) {
            outnum = val;
	    } else {
            outnum = val - 1;
	    }
	    lli a, b;
	    if (outnum % 2 == 0) {
            a = outnum / 2;
            b = outnum / 2 - 1;
	    } else {
            a = outnum / 2;
            b = a;
	    }

	    cout << "Case #" << c << ": ";
	    cout << a << " " << b;
	    cout << endl;
	}
	return 0;
}
