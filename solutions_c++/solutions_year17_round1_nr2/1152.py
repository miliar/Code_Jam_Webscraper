#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cassert>
//#include <functional>

using namespace std;
#define MP make_pair
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;


int q1[50][50];
int q2[50][50];
int q[50][50];
int r[50];
int n, p;

int idx[50];

int solve() {
    int tmp[50];
    int count = 0;
    for (int i = 0; i < p; i++) {
        memcpy(tmp, idx, sizeof(tmp));
        for (int k = q1[0][i]; k <= q2[0][i]; k++) {
            bool found = true;
            for (int j = 1; j < n; j++) {
                bool flag = false;
                for (int ii = tmp[j]; ii < p; ii++) {
                    if (q1[j][ii] <= k && q2[j][ii] >= k) {
                        tmp[j] = ii+1;
                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    found = false;
                    break;
                }
            }
            if (found) {
                memcpy(idx, tmp, sizeof(tmp));
                count++;
                break;
            }
        }
    }
    return count;
}

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> p;
        for (int j = 0; j < n; j++) {
            cin >> r[j];
        }
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < p; k++) {
                cin >> q[j][k];
            }
            sort(q[j], q[j] + p);
            for (int k = 0; k < p; k++) {
                q2[j][k] = (q[j][k] * 10) / (r[j] * 9);
                q1[j][k] = (q[j][k] * 10 + r[j]*11-1) / (r[j]*11);
            }
        }
        for (int j = 0; j < n; j++) {
            idx[j] = 0;
        }
        printf("Case #%d: %d\n", i, solve());
    }
}
