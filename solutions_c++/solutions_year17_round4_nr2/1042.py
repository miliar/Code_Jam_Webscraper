#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

vector<int> uses;
int n;

int check(int x)
{
    int left = 0;
    int promote = 0;
    int y;

    for(int i = 0; i < n; ++i)
    {
        y = min(left, x);
        if(uses[i] > x + y)
        {
            return -1;
        }

        if(uses[i] <= x)
        {
            left += x-uses[i];
        }else
        {
            left -= uses[i] - x;
            promote += uses[i] - x;
        }
    }
    return promote;
}

int main()
{
    string file_name = "B-small-attempt0";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        //cout << "test " << t+1 << endl;
        int c, m;
        f1 >> n >> c >> m;
        uses.resize(0);
        uses.resize(1000);

        vector<int> tickets(c, 0);

        int p, b;
        for(int i = 0; i < m; ++i)
        {
            f1 >> p >> b;
            tickets[b-1]++;
            uses[p-1]++;
        }

        int l = 1, r;
        for(int i = 0; i < c; ++i)
        {
            l = max(l, tickets[i]);
        }
        r = m;

        int mid;
        while(r-l > 1)
        {
            mid = (r + l) / 2;
            int z = check(mid);
            if(z == -1)
            {
                l = mid;
            }else
            {
                r = mid;
            }
        }
        int y, z;
        z = check(l);
        y = l;
        if(z == -1)
        {
            z = check(r);
            y = r;
        }
        f2 << y << ' ' << z << endl;

    }
    return 0;
}

