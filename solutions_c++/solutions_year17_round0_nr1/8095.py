#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t;
    fin >> t;
    for (int q = 0; q < t; q++)
    {
        string s;
        fin >> s;
        int k;
        fin >> k;
        string s2 = s;
        int ans1 = 0;
        int ans2 = 0;
        int i = 0;
        bool f1 = true;
        bool f2 = true;
        while (i < s.size())
        {
            if (s[i] == '+')
                i++;
            else
            {
                if (i + k > s.size())
                {
                    f1 = false;
                    break;
                }
                else
                {
                    for (int e = i; e < i + k; e++)
                        if (s[e] == '+')
                            s[e] = '-';
                        else
                            s[e] = '+';
                    i++;
                    ans1++;
                }
            }
        }
        i = s.size() - 1;
        while (i >= 0)
        {
            if (s2[i] == '+')
                i--;
            else
            {
                if (i - k < 0)
                {
                    f2 = false;
                    break;
                }
                else
                {
                    for (int e = i; e > i - k; e--)
                        if (s2[e] == '+')
                            s2[e] = '-';
                        else
                            s2[e] = '+';
                    i--;
                    ans2++;
                }
            }
        }

    if (f1 && f2)
        fout << "Case #" << q + 1 << ": " << min(ans1, ans2) << endl;
    else
        if (f1)
            fout << "Case #" << q + 1<< ": " << ans1 << endl;
    else
            if (f2)
                fout << "Case #" << q + 1<< ": " << ans2 << endl;
    else
                fout << "Case #" << q + 1<< ": " << "IMPOSSIBLE" << endl;

    }
    return 0;
}
