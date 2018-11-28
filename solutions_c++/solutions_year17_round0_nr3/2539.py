#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>

using namespace std;

void solve() {
    long long n, k;
    cin >> n >> k;
    long long rest = k;
    int curlvl = 0;
    long long len1 = n;
    long long len2 = n;
    long long cnt1 = 0, cnt2 = 1;

    while (true) {
        long long l11 = (len1 - 1) / 2;
        long long l12 = (len1 - 1) / 2 + bool((len1 - 1) % 2);
        if (len1 == 0) {
            l12 = 0;
        }
        long long l21 = (len2 - 1) / 2;
        long long l22 = (len2 - 1) / 2 + bool((len2 - 1) % 2);
        if (len2 == 0) {
            l22 = 0;
        }
        long long lens[4] = { l11, l12, l21, l22 };
        long long nlen1 = *min_element(begin(lens), end(lens));
        long long nlen2 = *max_element(begin(lens), end(lens));

        long long ncnt1 = cnt1 * (l11 == nlen1) + cnt1 * (l12 == nlen1) + cnt2 * (l21 == nlen1) + cnt2 * (l22 == nlen1);
        long long ncnt2 = cnt1 * (l11 == nlen2) + cnt1 * (l12 == nlen2) + cnt2 * (l21 == nlen2) + cnt2 * (l22 == nlen2);

        if (nlen1 == nlen2) {
            ncnt1 = 0;
        }

        if (rest > cnt1 + cnt2) {
            rest -= cnt1 + cnt2;
            len1 = nlen1;
            len2 = nlen2;
            cnt1 = ncnt1;
            cnt2 = ncnt2;
            continue;
        }

        if (rest <= cnt2) {
            cout << l22 << ' ' << l21 << '\n';
            return;
        }

        cout << l12 << ' ' << l11 << "\n";
        return;
    }
    throw runtime_error("123");
}

int main() {
    int ttt;
    cin >> ttt;
    for (int tt = 0; tt < ttt; tt++) {
        cout << "Case #" << tt + 1 << ": ";
        solve();
    }
}