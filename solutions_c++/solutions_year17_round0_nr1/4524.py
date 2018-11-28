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

short arr[MAXN];

int main()
{
    long long t, result, k;
    string s;
    fin >> t;
    long long strlen = 0;

    long long index;
    for (int testcase = 1; testcase <= t; testcase++)
    {
        result = 0;
        getline(fin, s);
        if (s.length() < 2)
            getline(fin,s);
        for (index = 0; index < s.length(); index++)
        {
            if (s[index] == '+')
            {
                arr[index] = 1;
                continue;
            }
            if (s[index] == '-')
            {
                arr[index] = 0;
                continue;
            }
            break;
        }

        strlen = index;
        index++;
        k = 0;

        while (index < s.length())
        {
            k *= 10;
            k += s[index] - '0';
            index++;
        }



        for (int i = 0; i <= strlen - k; i++)
        {
            if (arr[i] == 1)
                continue;

            result += 1;
            for (int j = 0; j < k; j++)
            {
                arr[i + j] ^= 1;
            }
        }

        for (int i = strlen - k; i < strlen; i++)
        {
            if (arr[i] == 0)
            {
                result = -1;
                break;
            }
        }

        fout << "Case #" << testcase << ": ";
        if (result == -1)
        {
            fout << "IMPOSSIBLE";
        }
        else
        {
            fout << result;
        }

        fout << "\n";
    }


}
