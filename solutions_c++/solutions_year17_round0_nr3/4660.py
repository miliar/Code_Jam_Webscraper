#include <list>
#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <limits>

#define min(a,b) ((a<b)?(a):(b))
//#define max(a,b) ((a>b)?(a):(b))
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
    long long t, rmax, rmin;

    fin >> t;

    long long n, k, current;
    for (int testcase = 1; testcase <= t; testcase++)
    {
        cout << testcase << "\n";
        rmax = 0;
        rmin = 0;
        fin >> n >> k;

        priority_queue<long long> q;

        q.push(n);
        while (--k)
        {
            current = q.top();
            q.pop();
            q.push((current - 1)/2);
            q.push(current/2);
        }

        current = q.top();


        rmin = (current - 1)/2;
        rmax = current/2;

        fout << "Case #" << testcase << ": ";
        fout << rmax << " " << rmin;

        fout << "\n";
    }


}
