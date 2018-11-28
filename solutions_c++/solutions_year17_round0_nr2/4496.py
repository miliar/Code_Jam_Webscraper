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

#define MAXN 20

//#define TEST
#ifndef TEST
ifstream fin("input.in");
ofstream fout("output.out");
#else
#define fin cin
#define fout cout
#endif

short arr[MAXN];


bool is_tidy(int n)
{
    for (int i = 1; i < n; i++)
    {
        if (arr[i - 1] > arr[i])
        {
            return false;
        }
        if (arr[i] < 0)
        {
            return false;
        }
    }
    return true;
}


int main()
{
    long long t, result;

    fin >> t;

    int n;
    string s;
    int slen;
    int start;
    int index;
    for (int testcase = 1; testcase <= t; testcase++)
    {
        result = 0;
        getline(fin, s);
        if (0 == s.length())
        {
            getline(fin, s);
        }
        slen = s.length();
        for (int i = 0; i < slen; i++)
        {
            arr[i] = s[i] - '0';
        }

        index = slen;
        while (index > 0)
        {
            if (is_tidy(slen))
                break;
            arr[index] = 9;
            arr[index  - 1] -= 1;
            index--;
        }

        start = 0;
        if (0 == arr[0])
            start = 1;

        fout << "Case #" << testcase << ": ";
        for (int i = start; i < slen; i++)
        {
            fout << arr[i];
        }

        fout << "\n";
    }


}
