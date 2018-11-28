#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <iomanip>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define forv(i, a) forn(i, (int)(a).size())

typedef long long lng;


double solve()
{
    int d, n;
    cin >> d >> n;
    
    double maxt = -1;
    forn(i, n)
    {
        int p, v;
        cin >> p >> v;
        maxt = max(maxt, 1.0 * (d - p) / v);
    }

    return d / maxt;
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0); 

    int T;
    cin >> T;
    forn(tc, T) {
        auto res = solve();

        std::cout << "Case #" << tc + 1 << ": " <<  setprecision(7) << fixed << res << endl;
    }
    
    return 0;
}
