#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#define ll long long
//#define sort(A) sort(A.begin(),A.end())
//#define rsort(A) sort(A.rbegin(),A.rend())
using namespace std;
static const ll D = 1000000007;
static const double PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

int main() {
    ll T, n, k;
    double res, U;
    cin >> T;
    for(ll t = 0; t<T; ++t){
        res = 1;
        cin >> n >> k >> U;
        vector<double> P(n);
        for(ll i =0; i<n; ++i)
            cin >> P[i];
        sort(P.begin(), P.end());
        while(P[n-1]>(accumulate(P.begin(), P.end(), 0.)+U)/n){
            res *= P[n-1];
            P.pop_back();
            --n;
        }
        cout << "Case #" << t+1 << ": " << fixed << setprecision(6) << res*pow((accumulate(P.begin(), P.end(), 0.)+U)/n, n) << endl;
    }
    return 0;
}
