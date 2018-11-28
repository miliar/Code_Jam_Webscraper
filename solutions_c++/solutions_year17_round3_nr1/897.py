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

long double PI = 3.14159265358979323846L;

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
        
        vector<pair<long double, long double>> cakes(n);
        for (int i = 0; i < n; ++i)
            infile>>cakes[i].first>>cakes[i].second;
    
        if (k == 1)
        {
            long double ans = 0;
            for (int i = k-1; i < n; ++i)
            {
                long double tempAns = PI * cakes[i].first * cakes[i].first + 2 * PI *  cakes[i].first * cakes[i].second;
                ans = max(ans, tempAns);
            }
            
            outfile<<"Case #"<<ca<<": "<<ans<<endl;
            continue;
        }
        
        sort(cakes.begin(), cakes.end());
        vector<long double> valueK_1(n, 0);
        
        priority_queue<long double> Q;
        long double s = 0;
        long double v;
        for (int i = 0; i < k-1; ++i)
        {
            v = cakes[i].first * cakes[i].second;
            s += v;
            Q.push(-v);
        }
        valueK_1[k-1] = s;
        for (int i = k; i < n; ++i)
        {
            long double v = -Q.top();
            long double vv = cakes[i-1].first * cakes[i-1].second;
            
            if (vv < v)
                valueK_1[i] = valueK_1[i-1];
            else
            {
                valueK_1[i] = valueK_1[i-1] + vv - v;
                Q.pop();
                Q.push(-vv);
            }
        }
        
        long double ans = 0;
        for (int i = k-1; i < n; ++i)
        {
            long double tempAns = 2*PI*valueK_1[i];
            tempAns += PI * cakes[i].first * cakes[i].first + 2 * PI *  cakes[i].first * cakes[i].second;
            ans = max(ans, tempAns);
        }
        
        outfile<<"Case #"<<ca<<": "<<ans<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}

