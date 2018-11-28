#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    int tests;
    cin >> tests;
    int counter = 1;
    while(tests)
    {
        double dest, n;
        cin >> dest >> n;
        double pos, speed;
        double max = 0;
        for(int i = 0; i < n; i++)
        {
            cin >> pos >> speed;
            double save = (dest - pos)/speed;
            if(save > max)
            {
                max = save;
            }
        }
        cout << "Case #" << counter++ << ": " << fixed << setprecision(6) << (dest/max) << endl;
        tests--;
    }
}
