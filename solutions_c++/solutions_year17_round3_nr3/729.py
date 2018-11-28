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

long double delta = 1e-7;

int main()
{
    ifstream infile;
    infile.open("/Users/Alex/Documents/algorithm/algorithm/in.data");
    
    ofstream outfile;
    outfile.open("/Users/Alex/Documents/algorithm/algorithm/out.data");
    
    int T;
    infile>>T;
    
    outfile.setf(ios::showpoint);
    outfile.precision(10);
    outfile.setf(ios::fixed);
    
    for (int ca = 1; ca <= T; ++ca)
    {
        int n, k;
        infile>>n>>k;
        
        long double u;
        infile>>u;
        
        vector<long double> a(n);

        for (int i = 0; i < n; ++i)
            infile>>a[i];
        
        sort(a.begin(), a.end());
        a.push_back(1.0);
        n += 1;

        for (int i = 0; i < n-1; ++i)
        {
            if (abs(u) < delta)
                break;

            if (a[i] < a[i+1])
            {
                long double diff = a[i+1] - a[i];
                if (diff * (i+1) <= u)
                {
                    for (int j = 0; j <= i; ++j)
                        a[j] = a[i+1];
                    u -= diff * (i+1);
                } else
                {
                    long double value = u / (i+1);
                    for (int j = 0; j <= i; ++j)
                        a[j] += value;
                    u = 0;
                    break;
                }
                
            }
        }
        
        long double ans = 1.0;
        for (int i = 0; i < n; ++i)
            ans *= a[i];
        
        outfile<<"Case #"<<ca<<": "<<ans<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}

