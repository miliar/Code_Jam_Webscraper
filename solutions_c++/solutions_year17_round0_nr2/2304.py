#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define forv(i, a) forn(i, (int)(a).size())

typedef long long lng;



string doit()
{
    string str;
    cin >> str;
    int n = str.size();

    int t = 1;
    while (t < n && str[t - 1] <= str[t])
        ++t;

    if (t == n)
    {
        return str;
    }

    while (t > 0 && str[t - 1] > str[t])
    {
        --t;
        --str[t];
    }

    for (int i = t + 1; i < n; ++i)
    {
        str[i] = '9';
    }
    
    return str;
}

lng solve()
{
    stringstream ss;
    ss << doit();

    lng res;
    ss >> res;

    return res;
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0); 

    int T;
    cin >> T;
    forn(tc, T) {
        auto res = solve();

        std::cout << "Case #" << tc + 1 << ": " << res << endl;
    }
    
    return 0;
}
