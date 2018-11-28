// In the Name of Allah
// AD13

#include <set>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;		//	typedef unsigned long long  ull;
typedef pair <int, int> pii;//	typedef pair <double, double> pdd;
#define MP make_pair
const int INF = 2147483647, MOD = 1000*1000*1000 + 7;
const double eps = 1e-8; // (eps < 1e-15) is the fact (1e-14)
#define For(i, n) for (int i = 0; i < (n); i++)
#define For1(i, n) for (int i = 1; i <= (n); i++)
//#define debug(x) { cerr << #x << " = _" << (x) << "_" << endl; }
void Error(string err) { cout << err; cerr << "_" << err << "_"; exit(0); }
int gcd(int a, int b) { return (b==0)? a: gcd(b, a%b); }
/*-------------------------------------------------------------------------------------*/

const int sz = 1000;

double p[sz];

/*_____________________________________________________________________________________*/

// think --> idea? --> really works?

int main() {
    //*
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    //*/

    cout.setf(ios::fixed);
    cout.precision(8);

    int T;
    cin >> T;
    For1 (tc, T) {
        //cerr << "--> " << tc << " / " << T << endl;
        int n;
        cin >> n >> n;
        double u;
        cin >> u;
        For(i, n) cin >> p[i];
        p[n] = 1;

        while (u > 0) {
            sort(p, p + n);
//            cout << "# "; For(i, n) cout << p[i] << ' '; cout << endl;
            for (int i = 0;; i++) {
                double dist = p[i + 1] - p[i];
                if (dist > 0) {
                    int from = i;
                    while (from > 0 && p[from - 1] == p[i]) from--;
                    int cnt = i - from + 1;
                    dist = min(u, dist * cnt);
//                    cout << "# " << dist << ' ' << from << ' ' << i << "->" << u << endl;
                    while (from <= i) p[from++] += dist / cnt;
                    u -= dist;
                    break;
                }
            }
        }

        double ans = 1;
        For(i, n) ans *= p[i];
        cout << "Case #" << tc << ": " << ans;
        cout << endl;
    }

    return 0;
}
/*

*/
