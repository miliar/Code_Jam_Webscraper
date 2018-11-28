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

int n, k;

int r[sz];
int h[sz];
double hh[sz];

const double pi = asin(1.0) * 2;

double solve(int st)
{
    vector<double> v;
    For(i, n) {
        if (i == st) continue;
        if (r[i] <= r[st]) v.push_back(hh[i]);
    }
    if (v.size() < k - 1) return 0;
    sort(v.begin(), v.end());

    double ans = pi * r[st]* r[st];
    ans += hh[st];

    for (int i = 1; i < k; i++) {
        ans += v[v.size() - i];
    }

    return ans;
}

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
        cin >> n >> k;

        For(i, n) {
            cin >> r[i] >> h[i];
            hh[i] = 2 * pi * r[i] * h[i];
        }

        double ans = 0;
        For(i, n) ans = max(ans, solve(i));

        cout << "Case #" << tc << ": " << ans;
        cout << endl;
    }

    return 0;
}
/*

*/
