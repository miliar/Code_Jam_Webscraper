#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;
struct cake
{
    double r, h;
    double area;
};
cake c[1003];
bool cmp(cake a, cake b)
{
    if (a.area > b.area)
        return true;
    else if (a.area < b.area)
        return false;
    else
        return a.r > b.r;
}
int main()
{
    int T;
    cin >> T;
    int n, k;
    for (int ca = 1; ca <= T; ++ca)
    {
        cin >> n >> k;
        for (int i = 0; i < n; i++)
        {
            cin >> c[i].r >> c[i].h;
            c[i].area = 2 * M_PI * c[i].r * c[i].h;
        }
        sort(c, c + n, cmp);
        double result = 0;
        double maxR = 0;
        for (int i = 0; i < n; ++i)
        {
            result = c[i].r * c[i].r * M_PI + c[i].area;
            int kk = 0;
            int j = 0;
            while (kk < k - 1)
            {
                if (i != j)
                    if (c[j].r <= c[i].r)
                    {
                        result += c[j].area;
                        kk++;
                    }
                j++;
            }
            if (result > maxR)
                maxR = result;
        }
        cout << "Case #" << ca << ": " << std::setprecision(25) << maxR << endl;
    }
}