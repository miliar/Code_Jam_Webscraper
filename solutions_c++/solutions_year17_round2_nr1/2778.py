#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.txt");
    int te;
    cin >> te;
    for (int tk = 0; tk < te; ++tk)
    {
        int d, n;
        cin >> d >> n;
        double time = 0;
        for (int i = 0; i < n; ++i)
        {
            int k;
            double s;
            cin >> k >> s;
            time = max(time, (d - k) / s);
        }
        cout << "Case #" << tk + 1 << ": ";
        cout.precision(26);
        cout << d / time << endl;
    }
    return 0;
}
