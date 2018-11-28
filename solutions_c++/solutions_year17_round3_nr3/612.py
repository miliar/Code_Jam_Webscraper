#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 2000;
const int inf = 1e9;
const int pp = 50 * 10000;

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int q;
    cin >> q;
    cout.precision(20);
    for (int t = 0; t < q; t++) {

        int n, k;
        long double s = 0;
        cin >> n >> k;
        cin >> s;
        int sum = (int)(s * pp);
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            long double x;
            cin >> x;
            a[i] = (int)(x * pp);
        }

        for (int i = 0; i < sum; i++) {
            int mina = inf;
            int id = -1;
            for (int j = 0; j < n; j++)
                if (a[j] < mina) {
                    mina = a[j];
                    id = j;
                }
            a[id]++;
        }

        long double p = 1;
        for (int i = 0; i < n; i++)
            p *= (long double)a[i] / pp;
        if (p > 1)
            p = 1;

        cout << "Case #" << t + 1 << ": " << p << "\n";
    }

    return 0;
}