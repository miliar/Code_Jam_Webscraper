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
        int ac, aj;
        infile>>ac>>aj;
        
        int ans = 0;
        
        if ((ac == 0 && aj == 1) || (ac == 1 && aj == 0))
        {
            int l, r;
            infile>>l>>r;
            
            ans = 2;
        }
        else if ((ac == 0 && aj == 2) || (ac == 2 && aj == 0))
        {
            int l1, l2, r1, r2;
            infile>>l1>>r1>>l2>>r2;
            if (l1 > l2)
            {
                int t = l1;
                l1 = l2;
                l2 = t;
                t = r1;
                r1 = r2;
                r2 = t;
            }
            
            int d1 = l1, d2 = l2-r1, d3 = 1440-r2;
            int maxG = max(d1, max(d2, d3));
            if (maxG >= 720 || (l1 + 1440-r2) >= 720)
                ans = 2;
            else
                ans = 4;
        }
        else
        {
            int l1, l2, r1, r2;
            infile>>l1>>r1>>l2>>r2;
            
            ans = 2;
        }
        
        outfile<<"Case #"<<ca<<": "<<ans<<endl;
        
    }

    infile.close();
    outfile.close();
    return 0;
}

