#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int ii, t;
    int d, n;
    int k, remaining;
    double s, time;
    ifstream f("cruise.in");
    ofstream g("cruise.out");
    f >> t;
    double maxTime;
    for (ii = 0; ii < t; ii++)
    {
        f >> d >> n;
        maxTime = 0;
        for (int i = 0; i < n; i++)
        {
            f >> k >> s;
            remaining = d - k;
            time = (double) remaining / s;
            if (time > maxTime)
            {
                maxTime = time;
            }
        }
        s = (double)d / maxTime;
        g << "Case #" << ii + 1 << ": ";
        g << fixed << setprecision(7) << s;
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}