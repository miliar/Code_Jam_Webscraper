#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
    ifstream fi;
    fi.open("A-large.in", ios::in);
    ofstream fo;
    fo.open("A-large_output.txt", ios::out);
    int t, k;
    fi >> t;
    char str[1001];
    for (int o = 1; o <= t; ++o)
    {
        fo << "Case #" << o << ": ";
        fi >> str;
        fi >> k;
        int i, j, counter = 0, n = strlen(str);
        for (i = 0; i <= n - k; ++i)
        {
            if (str[i] == '-')
            {
                ++counter;
                for (j = 0; j < k; ++j)
                    str[i + j] = (str[i + j] == '-'? '+': '-');
            }
        }
        for (; i < n; ++i)
            if (str[i] == '-')
                break;
        if (i != n)
            fo << "IMPOSSIBLE" << endl;
        else
            fo << counter << endl;
    }
}
