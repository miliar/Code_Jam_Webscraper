#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0; i < n; i++)
#define vvi vector<vector<int>>
#define vi vector<int>


pair<int, int> getPair(int k, bool* occ)
{
    int left[k];
    int right[k];
    forn(j, k)
    {
        if (occ[j])
        {
            left[j] = -1;
            continue;
        }
        if (j == 0)
            left[j] = 0;
        else
            left[j] = left[j-1] + 1;
    }

    for (int j = k - 1; j >= 0; j--)
    {
        if (occ[j])
        {
            right[j] = -1;
            continue;
        }
        if (j == k - 1)
            right[j] = 0;
        else
            right[j] = right[j+1] + 1;
    }

    int curmin = -1;
    int curmax = -1;
    int pos = -1;
    for (int j = k - 1; j >= 0; j--)
    {
        if (!occ[j])
        {
            if (curmin < min(left[j], right[j]))
            {
                curmin = min(left[j], right[j]);
                curmax = max(left[j], right[j]);
                pos = j;
            }
            else if (curmin == min(left[j], right[j]))
            {
                if (curmax <= max(left[j], right[j])) {
                    curmin = min(left[j], right[j]);
                    curmax = max(left[j], right[j]);
                    pos = j;
                }
            }
        }
    }
    occ[pos] = true;
    return make_pair(curmin, curmax);
};

int main() {
#ifndef ONLINE_JUDGE
   freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int TEST;
    cin >> TEST;
    forn(test, TEST)
    {
        int k, n;
        cin >> k >> n;
        k += 2;
        bool occ[k];
        memset(occ, 0, sizeof(occ));


        occ[0] = true;
        occ[k-1] = true;

        pair<int, int> p;
        forn(i, n)
        {
            p = getPair(k, occ);
        }




        printf("Case #%d: %d %d\n", test + 1, p.second, p.first);
    }


    return 0;
}