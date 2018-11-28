#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
ifstream ka("A-large (1).in");
ofstream ki("output.out");
int t, n;
double d, a, b;
int main()
{
    ka >> t;
    for(int j = 1; j <= t; j++)
    {
        ka >> d >> n;
        double maxim = -1.0;
        for(int i = 1; i <= n; i++)
        {
            ka >> a >> b;
            double timp = (d - a) / b;
            if(timp > maxim)
                maxim = timp;
        }
        //cout << j << " " << d << " " << maxim << '\n';
        ki << fixed <<  "Case #" << j << ": " << d / maxim << '\n';
    }
}
