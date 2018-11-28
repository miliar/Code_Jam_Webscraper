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
        long long int N, K;
        infile>>N>>K;
        
        long long int one = 1;
        int p = 0;
        
        while (true)
        {
            long long int v = (one<<p);
            if (K > v)
            {
                K -= v;
                p++;
            }
            else
            {
                break;
            }
        }
        
        long long int v = N;
        for (int i = 0; i < p; ++i) v >>= 1;
        
        long long int total_n = (one<<p);
        long long int total_sum = N;
        
        for (int i = 0; i < p; ++i)
            total_sum -= (one<<i);
        
        long long int num_v = total_sum - total_n * (v-1);
        
        if (K > num_v)
        {
            v--;
        }

        long long int l = 1;
        long long int r = v;
        long long int pos = (l+r)/2;
        
        long long int ls = pos - l;
        long long int rs = r - pos;
        outfile<<"Case #"<<ca<<": "<<max(ls, rs)<<" "<<min(ls, rs)<<endl;
        
        
        
        
        
        
        
    }

    infile.close();
    outfile.close();
    return 0;
}

