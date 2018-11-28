#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for(int t=1; t <= T; ++t)
    {
        string n;
        vector< pair<int, int> > digitGroups;

        cin >> n;
        int start = 0;
        for(int i=1; i < n.size(); ++i)
        {
            if(n[i] != n[i-1])
            {
                digitGroups.push_back(make_pair(n[i-1] - '0', i - start));
                start = i;
            }
        }
        digitGroups.push_back(make_pair(n[n.size()-1] - '0', n.size() - start));
        digitGroups.push_back(make_pair(10, 0));

        bool found = false;
        long long res = 0LL;
        for(int i=1; i < digitGroups.size(); ++i)
        {
            if(found)
            {
                for(int j=0; j < digitGroups[i-1].second; ++j)
                {
                    res = 10 * res + 9;
                }
            }
            else if(digitGroups[i].first < digitGroups[i-1].first)
            {
                found = true;
                res = 10 * res + (digitGroups[i-1].first - 1);
                for(int j=1; j < digitGroups[i-1].second; ++j)
                {
                    res = 10 * res + 9;
                }
            }
            else
            {
                for(int j=0; j < digitGroups[i-1].second; ++j)
                {
                    res = 10 * res + digitGroups[i-1].first;
                }
            }
        }
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
