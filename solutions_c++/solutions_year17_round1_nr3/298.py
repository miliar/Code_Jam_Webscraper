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
const int inf = 1e9;

int T,h1,a1,h2,a2,b,d;
int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        cin >> h1 >> a1 >> h2 >> a2 >> b >> d;
        int ans = 1000;
        for (int i = 0; i <= 100; i++) {
            for (int j = 0; j <= 100; j++) {
                int H1 = h1;
                int A1 = a1;
                int H2 = h2;
                int A2 = a2;
                int tmp = i+j;
                int k = 1;
                while (tmp <= 1000 && k <= j) {
                    if (H1-max(A2-d,0) <= 0) {
                        H1 = h1-A2;
                        tmp++;
                    } else {
                        A2 = max(A2-d,0);
                        H1 -= A2;
                        k++;
                    }
                }
                if (tmp < 1000) {
                    int k = 1;
                    while (k <= i && tmp <= 1000) {
                        if (H1 > A2) {
                            H1 -= A2;
                            k++;
                        } else {
                            H1 = h1-A2;
                            tmp++;
                        }
                    }
                    A1 += i*b;
                    while (H1 > 0 && H2 > 0 && tmp <= 1000) {
                        if (A1 < H2 && A2 >= H1) {
                            tmp++;
                            H1 = h1-A2;
                            if (H1 <= 0) {
                                break;
                            }
                        }
                        tmp++;
                        H1 -= A2;
                        H2 -= A1;
                    }
                    if (H2 <= 0) {
                        ans = min(tmp,ans);
                    }
                }
            }
        }
        if (ans >= 1000) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n",ans);
        }
        
    }
    return 0;
}
