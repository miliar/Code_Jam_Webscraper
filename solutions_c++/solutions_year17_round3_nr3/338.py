#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <valarray>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> pp;

const int CMAX = 55;
const int INF = 2e9 + 5;
const double eps = 1e-7;

bool eq(const double &a, const double &b) { return fabs(a-b) < eps; }

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        double a[CMAX];
        for (int i = 0; i < n; i++) cin >> a[i];
        sort(a, a+n);
        
        while (u > eps) {
            int cnt = 1;
            double dif = -1;
            for (int i = 1; i < n; i++) {
                if (!eq(a[i], a[0])) {
                    dif = a[i] - a[0];
                    break;
                }
                cnt++;
            }
            if (dif < 0) dif = 1.0 - a[0];
            
            double plus = (dif * (double)cnt > u) ? u / (double)cnt : dif;
            u -= plus * (double)cnt;
            for (int i = 0; i < cnt; i++) a[i] += plus;
        }
        
        double res = 1.0;
        for (int i = 0; i < n; i++) res *= a[i];
        
        cout << fixed << setprecision(10) << res << endl;
    }
    
    return 0;
}
