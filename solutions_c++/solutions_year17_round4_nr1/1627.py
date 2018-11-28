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

int a[5];

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
//    for (int i1 = 1; i1 <= 2; i1++)
//        for (int i2 = i1; i2 <= 2; i2++)
//            for (int i3 = i2; i3 <= 2; i3++)
//                for (int i4 = i3; i4 <= 2; i4++)
//                    for (int i5 = i4; i5 <= 3; i5++)
//                        if ((i1 + i2 + i3 + i4/* + i5*/) % 3 == 0)
//                            cout << i1 << " " << i2 << " " << i3 << " " << i4/* << " " << i5 */<< endl;
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        
        int n, p;
        cin >> n >> p;
        int x;
        for (int i = 0; i < 4; i++) a[i] = 0;
        for (int i = 0; i < n; i++) { cin >> x; a[x%p]++; }
        
        if (p == 2) cout << a[0] + (a[1] + 1) / 2 << endl;
        else if (p == 3) {
            int res = a[0];
            int pairs = min(a[1], a[2]);
            res += pairs;
            a[1] -= pairs;
            a[2] -= pairs;
            res += (a[1] + 2) / 3;
            res += (a[2] + 2) / 3;
            cout << res << endl;
        }
        else {
            
            
            
            
            
        }
    }
    
    return 0;
}
