#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream f("input.txt");
    ofstream g("output.txt");
    int n;
    f >> n;
    for (int test = 1;  test <= n; test++)
    {
        string s;
        int k;
        f >> s >> k;
        int l = s.size();
        int ret = 0;
        bool gata = false;
        int i = 0;
        while (!gata)
        {
            while (i < l && s[i] == '+')
                i++;
            if (i == l)
            {
                g << "Case #" << test << ": " << ret << "\n";
                gata = true;
                break;
            }
            if (i + k - 1 < l)
            {
                ret++;
                for (int pas = 0; pas < k; ++pas)
                {
                    if (s[i + pas] == '-')
                        s[i + pas] = '+';
                    else
                        s[i + pas] = '-';
                }
            }
            else
            {
                g << "Case #" << test << ": " << "IMPOSSIBLE" << "\n";
                gata = true;
                break;
            }
        }
    }

    return 0;
}
