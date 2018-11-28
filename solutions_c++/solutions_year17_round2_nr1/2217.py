#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class  Solution
{
public:
    double CruiseControl(double d, int n, vector<vector<int>> horses)
    {
        double time = (d - horses[0][0]) / horses[0][1];
        for (auto horse : horses)
        {
            time = max(time, (d - horse[0]) / horse[1]);
        }
       return d / time;
    }
};

void main() {
    int t;
    cin >> t;
    Solution sol;
    for (int i = 1; i <= t; ++i) {
        int d, n;
        cin >> d >> n;
        vector<vector<int>> horses;
        for (int j = 0; j < n; j++)
        {
            int k, s;
            cin >> k >> s;
            horses.push_back({k, s});
        }
        cout << fixed;
        cout.precision(6);
        cout << "Case #" << i << ": " << sol.CruiseControl(d, n, horses) << endl;
    }
}