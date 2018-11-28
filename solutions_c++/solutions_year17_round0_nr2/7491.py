#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bitset>
#include <ctime>
#include <algorithm>
#define ll long long
#define mp make_pair

using namespace std;

string s;
ll n, T;

ll powers[20];

ll cast(ll n, int pw = -1) {
    //cout << n << ' ' << pw << "\n";
    if (pw == -1) {
        ll nn = n;
        while (nn) {
            pw++;
            nn /= 10;
        }
    }
    if (pw == 0) return n;
    ll digit = (n / powers[pw]) % 10;
    for (int i = 0; i < pw; ++i) {
        if ((n / powers[i]) % 10 < digit) {
            n -= n % powers[i + 1];
            n -= 1;
            return cast(n, pw);
        }
    }
    return cast(n, pw - 1);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output", "w", stdout);

    powers[0] = 1;
    for (int i = 1; i < 20; ++i)
        powers[i] = powers[i - 1] * 10;

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n;
        
        n = cast(n);

        cout << "Case #" << t << ": ";
        cout << n << "\n";
    }

    return 0;
}

/*

3
2 2
5 2
222 4

*/