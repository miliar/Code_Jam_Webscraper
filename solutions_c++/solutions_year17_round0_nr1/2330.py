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

string str;

void flip(int start, int k)
{
    for (int i = start; i < start + k; ++i)
    {
        str[i] = (str[i] == '+' ? '-' : '+');
    }
}

int solve()
{
    int n, k;

    cin >> str >> k; 
    n = str.size();

    int res = 0;
    for (int i = 0; i <= n - k; ++i)
    {
        if (str[i] == '-') {
            ++res;
            flip(i, k);
        }
    }

    for (int i = n - k; i < n; ++i)
    {
        if (str[i] == '-')
        {
            return -1;
        }
    }

    return res;
}


int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0); 

    int T;
    cin >> T;
    forn(tc, T) {
        auto res = solve();

        std::cout << "Case #" << tc + 1 << ": ";
        
        if (res < 0) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << res;
        }
        
        cout << endl;
    }
    
    return 0;
}
