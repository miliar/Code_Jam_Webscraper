#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>
#include <queue>
#include <cstring>
#include <set>
#include <map>

using namespace std;

const int maxN = 110, oo = 23041997;

#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long
#define F first
#define S second
#define mp make_pair

int test, n, p, a[maxN][maxN], c[maxN], l[maxN], res;

int up(int i, int j) {
    double x = ((10.0 / 9) * a[i][j]) / c[i];
    return floor(x);
}

int low(int i, int j) {
    double x = ((10.0 / 11) * a[i][j]) / c[i];
    //cout << x << " " << ceil(x) << endl;
    return ceil(x);
}

int main() {
    scanf("%d\n", &test);
    foru(t, 1, test) {
        cin >> n >> p;
        res = 0;
        foru(i, 1, n) cin >> c[i];
        foru(i, 1, n)
            foru(j, 1, p) scanf("%d", &a[i][j]);
        foru(i, 1, n) sort(a[i] + 1, a[i] + p + 1), l[i] = 1;
        int x = 1;
        //cout << low(1, 1) << " " << up(1, 1) << endl;
        while (true) {
            foru(i, 1, n)
                while (l[i] <= p && up(i, l[i]) < x) ++l[i];
            while (true) {
                bool check = true;
                foru(i, 1, n)
                    if (l[i] > p || low(i, l[i]) > x) {
                        check = false;
                        break;
                    }
                if (check) {
                    foru(i, 1, n) ++l[i];
                    ++res;
                }
                else
                    break;
            }
            bool check = true;
            foru(i, 1, n)
                if (l[i] > p) {
                    check = false;
                    break;
                }
            if (!check) break;
            int minv = oo;
            foru(i, 1, n) {
                if (low(i, l[i]) > x) minv = min(minv, low(i, l[i]));
                if (up(i, l[i]) > x) minv = min(minv, up(i, l[i]));
            }
            if (minv == oo) ++x;
            else x = minv;
        }
        printf("Case #%d: %d\n", t, res);
    }
}
