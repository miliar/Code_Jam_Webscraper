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

const int sz = 10 * 1000;
int pos[sz];
int speed[sz];

/*_____________________________________________________________________________________*/

int main() {
    //*
    freopen("aa.in", "r", stdin);
    freopen("aa.out", "w", stdout);
    //*/

    cout.setf(ios::fixed);
    cout.precision(8);

    int T;
    cin >> T;
    For1 (tc, T) {
        //cerr << "--> " << tc << " / " << T << endl;

        int d, n;
        cin >> d >> n;
        For (i, n) {
            cin >> pos[i] >> speed[i];
        }

        double ans = 1e222;

        For (i, n) {
            double t = d - pos[i];
            t /= speed[i];
            ans = std::min(ans, d / t);
        }

        cout << "Case #" << tc << ": " << ans;
        cout << endl;
    }

    return 0;
}
/*

*/
