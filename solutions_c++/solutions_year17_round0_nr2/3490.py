#include <algorithm>
#include <iostream>
#include <cstdio>
#include <queue>
#define pii pair<int, int>
#define piii pair<pii, char*>
#define LL long long
using namespace std;

const int N = 110000;
int a[N];

int main ()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
    while (T--) {
        LL n, res = 0;
        int flag = 0, an = 0;
        cin >> n;
        while (n) a[++an] = n % 10, n /= 10;
        for (int i = an; i >= 1; i--) {
//            cout << a[i] << endl;
            if (flag) {
                res *= 10, res += 9;
                continue;
            }
            for (int j = 9; j >= 0; j--) {
                int ok = 1;
                for (int k = i; k >= 1; k--) {
                    if (a[k] > j) break;
                    if (a[k] < j) ok = 0;
                }
//                cout << j << ' ' << ok << endl;
                if (ok) {
                    res *= 10;
                    res += j;
                    if (a[i] > j) flag = 1;
                    break;
                }
            }
        }
        cout << "Case #" << cas++ << ": " << res << endl;
    }
}
