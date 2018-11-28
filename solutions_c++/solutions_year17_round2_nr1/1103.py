#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

typedef unsigned long long ull;
typedef signed long long ll;

int main()
{
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        ll D, N;
        cin >> D >> N;

        vector<pair<ll, ll> > horses;
        for(int i = 0; i < N; i++)
        {
            ll pos, speed;
            cin >> pos >> speed;
            horses.push_back(make_pair(pos, speed));
        }

        long double res = ((long double) (D) / (D - horses[0].first)) * horses[0].second;
        for(int i = 1; i < N; i++)
        {
            long double curr = ((long double) (D) / (D - horses[i].first)) * horses[i].second;
            res = min(res, curr);
        }

        cout << fixed << showpoint << setprecision(6) << "Case #" << t << ": " << res << endl;
    }

    return 0;
}