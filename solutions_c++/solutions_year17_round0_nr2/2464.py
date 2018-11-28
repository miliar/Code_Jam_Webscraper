#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
    ifstream fi;
    fi.open("B-large.in", ios::in);
    ofstream fo;
    fo.open("B-large.in_output.txt", ios::out);
    int t, n;
    fi >> t;
    char str[1001];
    for (int o = 1; o <= t; ++o)
    {
        fo << "Case #" << o << ": ";
        fi >> str;
        int len = strlen(str), i, j;
        for (i = 0; i < len - 1; ++i)
        {
            if (str[i] > str[i + 1])
            {
                for (j = i; j >= 0; --j)
                {
                    if (str[j] != str[i])
                        break;
                }
                str[++j] -= 1;
                for (++j; j < len; ++j)
                    str[j] = '9';
                break;
            }
        }
        for (i = 0; i < len; ++i)
            if (str[i] != '0') break;
        for (; i < len; ++i)
            fo << str[i];
        fo << endl;
    }
}
