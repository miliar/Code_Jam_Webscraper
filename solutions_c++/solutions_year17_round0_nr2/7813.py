#include <fstream>
#include <string.h>

using namespace std;

int main()
{
    ifstream fin("data.in");
    ofstream fout("data.out");
    int t;
    fin >> t;
    for (int test = 1; test <= t; test++)
    {
        char a[25];
        int n;
        fin >> a;
        n = strlen(a);
        for (int i = 0; i < n; i++)
        {
            a[i] = a[i] - '0';
        }
        for (int i = 0; i < n - 1; i++)
        {
            if (a[i] > a[i + 1])
            {
                a[i]--;
                int first = i + 1;
                for (int j = i - 1; j >= 0; j--)
                {
                    if (a[j] > a[j + 1])
                    {
                        a[j]--;
                        first = j + 1;
                    }
                }
                for (int j = first; j < n; j++)
                {
                    a[j] = char(9);
                }
                break;
            }
        }
        int start = n - 1;
        for (int i = 0; i < n; i++)
        {
            if (a[i] != 0)
            {
                start = i;
                break;
            }
        }
        fout << "Case #" << test << ": ";
        for (int i = start; i < n; i++)
        {
            fout << int(a[i]);
        }
        fout << '\n';
    }
    return 0;
}
