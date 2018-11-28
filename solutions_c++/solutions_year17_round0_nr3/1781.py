#include <bits/stdc++.h>
using namespace std;

#define int long long
#undef int
int main()
{
#define int long long
    int T;
    cin >> T;
    int kase = 0;
    while (T--) {
        cout << "Case #" << ++kase << ": ";
        int N, K;
        cin >> N >> K;
        int now = 0;
        int base = 1;
        int first;
        int second;
        first = N;
        second = N;
        int fb = 1, sb = 0;
        while ((now + base) < K) {
            int f = first;
            int s = second;
            int fb2 = fb;
            int sb2 = sb;
            if (f == s) {
                if (f % 2LL) {
                    fb = fb2 * 2LL + sb2 * 2LL;
                    sb = 0;
                    first = f / 2LL;
                    second = f / 2LL;
                } else {
                    fb = fb2 + sb2;
                    sb = fb2 + sb2;
                    first = f / 2LL;
                    second = (f - 1LL) / 2LL;
                }

            } else {
                if (f % 2LL) {
                    fb = fb2 * 2LL + sb2;
                    sb = sb2;
                    first = f / 2LL;
                    second = (s - 1LL) / 2LL;
                } else {
                    fb = fb2;
                    sb = fb2 + sb2 * 2LL;
                    first = f / 2LL;
                    second = s / 2LL;
                }
            }
            //cout << first << "* " << fb << " " << second << "* " << sb << endl;
            now += base;
            base <<= 1LL;
        }
        //cout << now << " " << fb << " " << sb << " " << first << " " << second << "  " << K << endl;
        if (now + fb >= K) {
            if (first % 2LL) {
                cout << first / 2LL << " " << first / 2LL << endl;
            } else {
                cout << first / 2LL << " " << (first - 1LL) / 2LL << endl;
            }
        } else {
            if (second % 2LL) {
                cout << second / 2LL << " " << second / 2LL << endl;
            } else {
                cout << second / 2LL << " " << (second - 1LL) / 2LL << endl;
            }
        }
    }
    return 0;
}
