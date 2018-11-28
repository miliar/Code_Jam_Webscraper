#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename S>
bool sorter(pair<T, S> a, pair<T, S> b)
{
    return a.first < b.first;
}
template bool sorter<int, int>(pair<int, int>, pair<int, int>);
template bool sorter<double, int>(pair<double, int>, pair<double, int>);


double findAnswer(vector<pair<int, int>> horses, int destination)
{
    double steps = 0.0;
    for (auto h : horses) {
        double k1 = h.first;
        double s1 = h.second;
        steps = max(steps, (destination - k1) / s1);
    }

    return destination / steps;
}


int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    cout << fixed << setprecision(6);

    long d;
    long n;
    for (int i = 1; i <= t; ++i) {
        cin >> d >> n;

        map<int, int> horses;
        for (int h = 1; h <= n; ++h) {
            long k;
            long s;
            cin >> k >> s;
            horses[k] = s;
        }
        horses[d] = 0;

        // positions
        vector<pair<int, int>> sortedHorses(horses.begin(), horses.end());
        sort(sortedHorses.begin(), sortedHorses.end(), &sorter<int, int>);

        cout << "Case #" << i << ": " << findAnswer(sortedHorses, d) << endl;
    }

    return 0;
}
