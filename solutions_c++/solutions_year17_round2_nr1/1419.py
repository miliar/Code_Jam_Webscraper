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

const int CMAX = 1e5 + 5;
const int INF = 2e9 + 5;

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        double time = 0;
        int d, n; cin >> d >> n;
        for (int i = 0; i < n; i++) {
            int k, s; cin >> k >> s;
            time = max(time, (double)(d-k)/(double)s);
        }
        cout << "Case #" << t << ": " << fixed << setprecision(10) << (double)d / time << endl;
    }
    
    return 0;
}
