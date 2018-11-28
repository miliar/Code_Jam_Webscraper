#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <functional>
#include <limits>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout.precision(numeric_limits<double>::max_digits10);

    int NR;

    cin >> NR;
    for(int r = 1; r <= NR; r++)
    {
        cout << "Case #" << r << ": ";

        double D, N;
        cin >> D >> N;
        double maxi = 0;
        for(int i = 0; i < N; i++)
        {
            double K, S;
            cin >> K >> S;

            double distance = D - K;
            double time = distance / S;
            maxi = max(maxi, time);
        }
        cout << (D / maxi) << endl;
    }

    return 0;
}
