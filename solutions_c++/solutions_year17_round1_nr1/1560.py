#include <list>
#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

#define min(a,b) ((a<b)?(a):(b))
#define max(a,b) ((a>b)?(a):(b))
#define abs(a) ((a>0)?(a):((-1)*a))

using namespace std;

#define MAXN 1005

//#define TEST
#ifndef TEST
ifstream fin("input.in");
ofstream fout("output.out");
#else
#define fin cin
#define fout cout
#endif

int main()
{
    long long t, result;
    string s;
    string s_prev;
    bool found_line = false;
    fin >> t;

    long long index;
    int repeates_print;
    char last_letter;
    int n, m;
    for (int testcase = 1; testcase <= t; testcase++)
    {
        repeates_print = 1;
        fin >> n >> m;
        found_line = false;
        cout << n << " " << m << "\n";
        fout << "Case #" << testcase << ":\n";
        for (int line = 0; line < n; line++)
        {
            result = 0;
            getline(fin, s);
            if (s.length() < 1)
                getline(fin,s);
            cout << s << "\n";
            for (index = 0; index < s.length(); index++)
            {
                if ('?' == s[index] && 0 == result)
                {
                    continue;
                }
                if ('?' == s[index] && 1 == result)
                {
                    s[index] = last_letter;
                }

                last_letter = s[index];
                if (0 == result)
                {
                    result = 1;
                    for (int j = 0; j < index; j++)
                    {
                        s[j] = last_letter;
                    }
                }
            }


            if (0 == result && !found_line)
            {
                repeates_print++;
                continue;
            }
            if (0 == result && found_line)
            {
                fout << s_prev << "\n";
                continue;
            }
            if (1 == result && !found_line)
            {
                while(repeates_print--)
                {
                    fout << s << "\n";
                }
                s_prev = s;
                found_line = true;
                continue;
            }
            if (1 == result && found_line)
            {
                fout << s << "\n";
                s_prev = s;
            }

        }
    }


}
