#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <functional>
#include <string>
#include <cstdlib>
#include <set>
#include <unordered_set>
#include <stdio.h>
#include <ctime>
#include <memory.h>
using namespace std;


int main()
{
    ifstream infile;
    infile.open("/Users/Alex/Documents/algorithm/algorithm/in.data");
    
    ofstream outfile;
    outfile.open("/Users/Alex/Documents/algorithm/algorithm/out.data");
    
    int T;
    infile>>T;
    
    for (int ca = 1; ca <= T; ++ca)
    {
        string s;
        int k;
        
        infile>>s>>k;
        int ans = 0;
        int n = s.length();
        
        for (int i = 0; i <= n-k; ++i)
        {
            if (s[i] == '-')
            {
                ++ans;
                for (int j = 0; j < k; ++j)
                {
                    int id = i+j;
                    if (s[id] == '-') s[id] = '+';
                    else s[id] = '-';
                }
            }
        }
        
        for (int i = 0; i < n; ++i)
        {
            if (s[i] == '-')
            {
                ans = -1;
                break;
            }
        }
        
        if (ans >= 0)
            outfile<<"Case #"<<ca<<": "<<ans<<endl;
        else
            outfile<<"Case #"<<ca<<": "<<"IMPOSSIBLE"<<endl;
        
        
    }

    infile.close();
    outfile.close();
    return 0;
}

