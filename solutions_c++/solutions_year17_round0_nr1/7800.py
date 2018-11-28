#include <string.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("data.in");
    ofstream fout("data.out");
    int n, k, t;
    char s[1005];
    fin >> t;
    for(int test = 1; test <= t; test++)
    {
        int changes = 0;
        fin >> s;
        fin >> k;
        n = strlen(s);
        for (int i = 0; i < n - k + 1; i++)
        {
            if (s[i] == '-')
            {
                changes++;
                for (int j = 0; j < k && i + j < n; j++)
                {
                    if (s[i + j] == '-')
                    {
                        s[i + j] = '+';
                    }
                    else
                    {
                        s[i + j] = '-';
                    }
                }
            }
        }
        for (int i = n - k + 1; i < n; i++)
        {
            if (s[i] == '-')
            {
                changes = -1;
            }
        }
        fout << "Case #" << test << ": ";
        if (changes >= 0)
        {
            fout << changes;
        }
        else
        {
            fout << "IMPOSSIBLE";
        }
        fout << '\n';
    }
    return 0;
}
