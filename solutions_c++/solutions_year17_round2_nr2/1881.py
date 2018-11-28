#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cassert>

#define INF 1000000000

using namespace std;

using ullong = unsigned long long;
using llong = long long;

template<typename T>
T Pow(T a, T n)
{
    T res = 1;
    while (n)
    {
        if (n & 1)
            res *= a;
        a *= a;
        n >>= 1;
    }
    return res;
}

int main()
{
    int t;
    cin >> t;
    const string imp = "IMPOSSIBLE";
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        string s;
        int n;
        cin >> n;
        int i,j;
        vector<int> a(6);
        vector<int> b(3);
        //char colors = {'R', 'O', 'Y', 'G', 'B', 'V'};
        char colors[3] = {'R', 'Y', 'B'};
        for(i=0; i<(int)a.size();++i)
        {
            cin >> a[i];
            if (i % 2 == 0)
            {
                b[i/2] = a[i];
            }
        }

        for(i=0; i<n; ++i)
        {
            int t = -1;
            int tmax = 0;
            for(j=0; j<(int)b.size(); ++j)
                if (b[j] > tmax)
                {
                    if (s.size() == 0 ||
                        s[s.size()-1] != colors[j])
                    {
                        t = j;
                        tmax = b[j];
                    }
                }
            if (t == -1)
            {
                s = imp;
                break;
            }
            if (s.size() > 0 &&
                b[0] <=1 && b[1] <=1 && b[2] <=1)
            {
                int k = 0;
                for (k=0; k<3; ++k)
                    if (colors[k] == s[0] &&
                        s[s.size()-1] != colors[k])
                {
                    if (b[k] == 1)
                    {
                        t = k;
                        break;
                    }
                }
            }
            --b[t];
            s.push_back(colors[t]);
        }

        if (s != imp)
        {
            for(i=0; i<n; ++i)
                if (s[i] == s[(i+1)%n])
            {
                s = imp;
                break;
            }
        }

        cout << "Case #" << tidx << ": ";
        cout << s;
        cout << endl;
    }
    return 0;
}
