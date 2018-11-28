#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef uint64_t llu;
typedef int64_t ll;

typedef pair<double, double> pll;

int main()
{
    int n = 0;
    cin >> n;

    for (int c = 0; c < n; c++)
    {
        double ans = 0.0;
        double dest = 0.0;
        llu h;
        cin >> dest;
        cin >> h;
        vector<pll> vec;

        for (int i = 0; i < h; i++)
        {
            pll h;
            cin >> h.first;
            cin >> h.second;
            vec.push_back(h);
        }

        //sort(vec.begin(), vec.end(), [](pll a, pll b) {return a.first > b.first; });

        double max = 0.0;
        for (int i = 0; i < vec.size(); i++)
        {
            // find the slowest horse?
            double ttg = (dest - vec[i].first) / vec[i].second;
            if (ttg > max)
            {
                max = ttg;
            }
        }
        ans = dest / max;
        std::cout.precision(6);
        cout <<fixed << "Case #" << c + 1 << ": " << ans << endl;
    }

    return 0;
}