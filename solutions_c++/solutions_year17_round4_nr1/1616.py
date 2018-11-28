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


int main()
{
    string file_name = "A-small-attempt0";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        int n, p;
        f1 >> n >> p;
        vector<int> g(5, 0);
        int x;
        for(int i = 0; i < n; ++i)
        {
            f1 >> x;
            g[x % p]++;
        }
        int ans = 0;
        ans += g[0];
        g[0] = 0;
        if(p == 2)
        {
            ans += g[1] / 2;
            if(g[1] % 2)
            {
                ans++;
            }
        }else if(p == 3)
        {
            x = min(g[1], g[2]);
            ans += x;
            g[1] -= x;
            g[2] -= x;
            if(g[1])
            {
                ans += g[1] / 3;
                if(g[1] % 3)
                {
                    ans++;
                }
            }else
            {
                ans += g[2] / 3;
                if(g[2] % 3)
                {
                    ans++;
                }
            }
        }else
        {
            x = min(g[1], g[3]);
            ans += x;
            g[1] -= x;
            g[3] -= x;
            x = g[2] / 2;
            ans += x;
            g[2] -= x * 2;
            x = max(g[1], g[3]) / 4;
            ans += x;
            if(g[1])
            {
                g[1] -= x * 4;
            }else
            {
                g[3] -= x * 4;
            }

            if(g[2] && max(g[1], g[3]) >= 2)
            {
                g[2] = 0;
                if(g[1])
                {
                    g[1] -= 2;
                }else
                {
                    g[3] -= 2;
                }
            }
            if(g[1] + g[2] + g[3] >= 0)
            {
                ans++;
            }
        }
        f2 << ans << endl;
    }
    return 0;
}

