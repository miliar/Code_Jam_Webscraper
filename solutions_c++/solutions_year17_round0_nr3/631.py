#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <algorithm>

#define mp make_pair
#define pb push_back

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 1e6;
const int inf = 1e9 + 5;

int main() {
    /*std::ios::sync_with_stdio(false);
    cin.tie(0);*/
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int q;
    cin >> q;
    for (int t = 0; t < q; t++) {

        long long n, k;
        cin >> n >> k;

        long long count = 0;
        long long len = n;
        long long c1 = 1;
        long long c2 = 0;
        while (((long long)1 << count) < k) {
            k = k - ((long long)1 << count);
            count++;

            long long c11, c22;
            if (len % 2 == 1) {
                c11 = c1 * 2 + c2;
                c22 = c2;
            } else {
                c11 = c1;
                c22 = c1 + c2 * 2;
            }
            c1 = c11;
            c2 = c22;
            len = (len - 1) / 2;
        }

        if (c2 >= k) {
            cout << "Case #" << t + 1 << ": "  << (len + 1) / 2 << " " << len / 2 << "\n";
        } else
            cout << "Case #" << t + 1 << ": "  << len / 2 << " " << (len - 1) / 2 << "\n";
    }

    return 0;
}