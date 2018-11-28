#include <iostream>
#include <fstream>
#include <vector>
#include <climits>
#include <cfloat>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    ifstream inf;
    inf.open("C:\\Work\\ALGO\\CF\\ladder.txt");
    ofstream off;
    off.open("C:\\Work\\ALGO\\CF\\ladder_oo.txt");
    int t;
    inf >> t;
    off.setf(ios::fixed);
    off.precision(7);
    for(int i = 0; i < t; ++i)
    {
        double ans = DBL_MAX;
        long long r, n;
        inf >> r >> n;
        for(int j = 0; j < n; ++j)
        {
            long long cur_p, cur_v;
            inf >> cur_p >> cur_v;
            ans = min(ans, (double(r)/double(r - cur_p)) * cur_v);
            if(ans < 0)
            {
                int gg = 0;
            }
        }
        off << setw(6) <<"Case #" << i + 1 <<": " << ans <<endl;
    }
    off.close();
    inf.close();
    return 0;
}