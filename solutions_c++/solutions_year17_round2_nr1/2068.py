#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    ios_base::sync_with_stdio(false);
    int t, i, j;
    cin >> t;
    for (i = 0; i < t; i++)
    {
        int d, n, s, k;
        double ans = 0;
        cin >> d >> n;
        for (j = 0; j < n; j++)
        {
            cin >> k >> s;
            double cur = d - k;
            cur /= s;
            ans = max(ans, cur);
        }
        double cur = d;
        cur /= ans;
        cout << "Case #" << i+1 << ": " << fixed << setprecision(9) << cur << endl;
    }
    return 0;
}
