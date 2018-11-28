#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iomanip>
#include <map>
#include <cmath>
#include <deque>
using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef pair<ll,ll> l4;
const int maxn = 200010;
const double eps = 1e-8;

int T;
ll n,k;
ll mi,ma,n1,n2;
int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        cin >> n >> k;
        ll cur = 1;
        ma = n;
        n1 = 1;
        mi = 0;
        n2 = 0;
        while (cur < k) {
            k -= cur;
            mi--;
            ma--;
            ll maxi = ma-ma/2;
            ll mini = maxi-1;
            ll tn1 = 0;
            ll tn2 = 0;
            if (ma/2 > 0) {
                if (ma/2 == maxi) {
                    tn1 += n1;
                } else {
                    tn2 += n1;
                }
            }
            if (ma-ma/2 > 0) {
                if (ma-ma/2 == maxi) {
                    tn1 += n1;
                } else {
                    tn2 += n1;
                }
            }
            if (mi/2 > 0) {
                if (mi/2 == maxi) {
                    tn1 += n2;
                } else {
                    tn2 += n2;
                }
            }
            if (mi-mi/2 > 0) {
                if (mi-mi/2 == maxi) {
                    tn1 += n2;
                } else {
                    tn2 += n2;
                }
            }
            ma = maxi;
            mi = mini;
            n1 = tn1;
            n2 = tn2;
            cur = n1+n2;
        }
        if (k <= n1) {
            ma--;
            cout << ma-ma/2 << " " << ma/2 << endl;
        } else {
            mi--;
            cout << mi-mi/2 << " " << mi/2 << endl;
        }
    }
    return 0;
}
