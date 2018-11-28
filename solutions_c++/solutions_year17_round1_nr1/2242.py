#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

#define INF 1000000000

using namespace std;

using ullong = unsigned long long;
using llong = long long;

int ordinal(char c)
{
    return c - 'A';
}

int main()
{
    int t;
    cin >> t;
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        int r = 0;
        int c = 0;
        vector<string> d;
        string s;
        int i, j, x, y, k;
        cin >> r >> c;
        for(i=0; i<r; ++i)
        {
            cin >> s;
            d.push_back(s);
        }


        int left, right, top, bottom;
        vector<bool> used(26);

        for(i=0; i<r; ++i)
            for(j=0; j<c; ++j)
        {
            if (d[i][j] != '?' &&
                !used[ordinal(d[i][j])])
            {
                for (x=i-1; x>=0 && d[x][j] == '?'; --x);
                left = x + 1;
                for (x=i+1; x<r && d[x][j] == '?'; ++x);
                right = x - 1;
                for (k=left; k<=right; ++k)
                    d[k][j] = d[i][j];
                used[ordinal(d[i][j])] = true;
            }
        }

        used.assign(26, false);

        for(i=0; i<r; ++i)
            for(j=0; j<c; ++j)
        {
            if (d[i][j] != '?' &&
                !used[ordinal(d[i][j])])
            {
                left = i;
                for(k=i+1; k<r && d[k][j] == d[i][j]; ++k);
                right = k - 1;

                bool canExpand = true;
                y = j;
                while (canExpand && (y-1) >= 0)
                {
                    for (k=left; k<=right && canExpand; ++k)
                        if (d[k][y-1] != '?')
                            canExpand = false;
                    if (canExpand)
                        --y;
                }
                bottom = y;

                canExpand = true;
                y = j;
                while (canExpand && (y+1) >= 0)
                {
                    for (k=left; k<=right && canExpand; ++k)
                        if (d[k][y+1] != '?')
                            canExpand = false;
                    if (canExpand)
                        ++y;
                }
                top = y;

                for (x=left; x<=right; ++x)
                    for (y=bottom; y<=top; ++y)
                        d[x][y] = d[i][j];

                used[ordinal(d[i][j])] = true;
            }
        }

        cout << "Case #" << tidx << ":\n";
        for (i=0; i<r; ++i) {
            cout << d[i] << endl;
        }
    }
    return 0;
}
