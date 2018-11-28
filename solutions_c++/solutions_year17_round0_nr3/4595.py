#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

long long bathroomStalls(long long n, long long k) {
    long long val = k;
    long long bit = 1;
    long long bitholder;
    while (val >>= 1) {
        bit <<= 1;
    }

    bitholder = bit;
    val = n;
    bit >>= 1;
    while (bit > 0) {
        val = (val-1)/2;
        bit >>= 1;
    }
    long long count = n - val*bitholder - bitholder + 1;
    
    if (k - bitholder < count && count > 0)
        return val + 1;
    else
        return val;
}

int main() {

    string name = "C-large";
	string path = "";

	freopen((path + name + ".in").c_str(), "r", stdin);
	freopen((path + name + ".out").c_str(), "w", stdout);

	int cases;
	cin >> cases;

    long long n, k;
    long long val;
	for (int prob = 1; prob <= cases; prob++) {
        cin >> n >> k;
        val = bathroomStalls(n, k);
        
		printf("Case #%d: %lld %lld\n", prob, val/2, (val-1)/2);
	}

	return 0;
}
