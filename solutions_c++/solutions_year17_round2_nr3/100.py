#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

const int N = 100 + 5;

int n, q;
int e[N], s[N];
long long a[N][N];
long double d[N];

void solve()
{
    cin >> n >> q;
    for(int i = 0; i < n; ++ i) {
        cin >> e[i] >> s[i];
    }
    for(int i = 0; i < n; ++ i) {
        for(int j = 0; j < n; ++ j) {
            cin >> a[i][j];
        }
        a[i][i] = 0;
    }
    for(int k = 0; k < n; ++ k) {
        for(int i = 0; i < n; ++ i) {
            for(int j = 0; j < n; ++ j) {
                if (a[i][k] >= 0 && a[k][j] >= 0) {
                    if (a[i][j] < 0 || a[i][j] > a[i][k] + a[k][j]) {
                        a[i][j] = a[i][k] + a[k][j];
                    }
                }
            }
        }
    }

    for(int i = 0; i < q; ++ i) {
        int s, t;
        cin >> s >> t;
        --s, --t;
        for(int j = 0; j < n; ++ j) {
            d[j] = -1;
        }
        d[s] = 0;
        for(int j = 0; j < n; ++ j) {
            for(int k = 0; k < n; ++ k) {
                if (d[k] < 0) continue;
                for(int l = 0; l < n; ++ l) {
                    if (a[k][l] >= 0 && a[k][l] <= e[k]) {
                        long double tmp = 1.0 * a[k][l] / ::s[k];
                        if (d[l] < 0 || d[l] > d[k] + tmp) {
                            d[l] = d[k] + tmp;
                        }
                    }
                }
            }
        }
        printf(" %.10f", (double)d[t]);
    }
    cout << endl;
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d:", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}
