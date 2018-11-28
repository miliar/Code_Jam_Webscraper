#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int a[30];

int main()
{
    int nr_tests;

    ifstream f("input.txt");
    ofstream g("output.txt");
    f >> nr_tests;

    for (int test = 1; test <= nr_tests; ++test)
    {
        long long x;
        f >> x;
        int n = 0;
        while(x > 0)
        {
            a[++n] = x % 10;
            x = x / 10;
        }
        reverse(a+1, a+n+1);
        bool ok = true;
        int badPosition;
        for (int i = 2; i <= n; ++i)
        {
            if (a[i] < a[i-1])
            {
                badPosition = i-1;
                ok = false;
                break;
            }
        }

        if (ok)
        {
            g << "Case #" << test << ": ";
            for (int i = 1; i <= n; ++i)
            {
                g << a[i];
            }
            g << "\n";
        }
        else
        {
            while(badPosition > 1)
            {
                if (a[badPosition] <= a[badPosition - 1])
                {
                    badPosition--;
                }
                else
                {
                    break;
                }
            }
            if (badPosition == 1 && a[1] == 1)
            {
                g << "Case #" << test << ": ";
                for (int i = 1; i < n; ++i)
                {
                    g << 9;
                }
                g << "\n";
            }
            else
            {
                a[badPosition]--;
                g << "Case #" << test << ": ";
                for (int i = 1; i <= badPosition; ++i)
                {
                    g << a[i];
                }
                for (int i = badPosition + 1; i <= n; ++i)
                {
                    g << 9;
                }
                g << "\n";
            }
        }
    }

    f.close();
    g.close();

    return 0;
}
