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

void solve(string &a)
{
    for (int i = a.length()-2; i >= 0; --i)
    {
        if (a[i] > a[i+1])
        {
            a[i] -= 1;
            for (int j = i+1; j < a.size(); ++j) a[j] = '9';
        }
    }
}


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
        infile>>s;
        
        solve(s);
        
        int pos = -1;
        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] != '0')
            {
                pos = i;
                break;
            }
        }
        
        outfile<<"Case #"<<ca<<": "<<s.substr(pos, s.length()-pos)<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}

