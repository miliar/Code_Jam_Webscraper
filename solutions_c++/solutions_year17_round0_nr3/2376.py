#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define forv(i, a) forn(i, (int)(a).size())

typedef long long lng;

pair<lng, lng> solve(lng n, lng k)
{
    map<lng, lng, greater<lng>> d;
    d[n] = 1;
    lng top = 1;

    while (k > top)
    {
        k-= top;
        if (n%2 == 1)
        {
            d[(n - 1)/2] += 2 * top;
        }
        else
        {
            d[n/2 - 1] += top;
            d[n/2] += top;
        }

        d.erase(d.begin());
        auto it = d.begin();
        n = it->first;
        top = it->second;
    }

    if (n % 2 == 1) 
    {
        return make_pair((n - 1)/2, (n - 1)/2);
    }
    else
    {
        return make_pair(n/2, n/2 - 1);
    }
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0); 

    int T;
    cin >> T;
    forn(tc, T) {
        lng n, k;
        cin >> n >> k;
        auto res = solve(n, k);

        std::cout << "Case #" << tc + 1 << ": " << res.first << " " << res.second << endl;
    }
    
    return 0;
}
