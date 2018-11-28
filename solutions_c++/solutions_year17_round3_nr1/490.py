#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

bool cmp(const pair<long long int,long long int> &a, const pair<long long int,long long int> &b)
{
    return a.first*a.second > b.first*b.second;
}

int main()
{
    string file_name = "A-large";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        int n, k;
        f1 >> n >> k;
        int r, h;
        vector< pair<long long int,long long int> > puncake(n);
        long long bestans = -1;
        for(int i = 0; i < n; ++i)
        {
            f1 >> r >> h;
            puncake[i] = make_pair(r, h);
        }
        sort(puncake.begin(), puncake.end(), cmp);

        pair<long long int,long long int> f;
        for(int i = 0; i < n; ++i)
        {
            f = puncake[i];
            long long int ans = 0;
            int count = 1;
            ans = f.first * f.first;
            //cout << ans << ' ';
            ans += 2 * f.first * f.second;
            //cout << ans << endl;
            for(int j = 0; j < n; ++j)
            {
                if(count == k)break;
                if(i == j)continue;
                if(puncake[j].first > f.first)continue;
                ans += 2 * puncake[j].first * puncake[j].second;
                count++;
            }
            if(count == k && ans > bestans)
            {
                bestans = ans;
                //cout << t << ' ' << ans << ' ' << i << ' ' << f.first << endl;
            }
        }

        long double ans = bestans;
        ans = ans * M_PI;

        f2.flags(ios::fixed);
        f2 << setprecision(8) << ans << endl;
    }
    return 0;
}

