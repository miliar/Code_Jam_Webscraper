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
const int maxn = 50010;
const double eps = 1e-8;

int T,n,p;
int tar[100];
double target[100];
int ing[100][100];

int com(double x) {
    if (x > eps) {
        return 1;
    }
    if (x < -eps) {
        return -1;
    }
    return 0;
}

int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        cin >> n >> p;
        for (int i = 0; i < n; i++) {
            cin >> tar[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                cin >> ing[i][j];
            }
            sort(ing[i],ing[i]+p);
        }
        int ans = 0;
        for (int mul = 1; ; mul++) {
            bool end = 0;
            for (int i = 0; i < n; i++) {
                target[i] = (double)mul*tar[i];
                if (target[i]/1.2 > ing[i][p-1]) {
                    end = 1;
                }
            }
            if (end) {
                break;
            }
            int ok = 100;
            for (int i = 0; i < n; i++) {
                int tmp = 0;
                for (int j = 0; j < p; j++) {
                    if (com(target[i]*0.9-ing[i][j])<=0 && com(target[i]*1.1-ing[i][j])>=0) {
                        tmp++;
                    } else if (com(target[i]*1.1-ing[i][j])<0) {
                        break;
                    }
                }
                ok = min(ok,tmp);
                if (ok == 0) {
                    break;
                }
            }
            ans += ok;
            if (ok) {
                for (int i = 0; i < n; i++) {
                    int tmp = ok;
                    for (int j = 0; j < p; j++) {
                        if (com(target[i]*0.9-ing[i][j])<=0 && com(target[i]*1.1-ing[i][j])>=0) {
                            tmp--;
                            ing[i][j] = -1;
                        }
                        if (tmp == 0) {
                            break;
                        }
                    }
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}
