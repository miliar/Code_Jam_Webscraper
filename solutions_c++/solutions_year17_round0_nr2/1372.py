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


int is_tidy(string s)
{
    int ind = -1;
    for(int i = 1; i < s.size(); ++i)
    {
        if(s[i-1] > s[i])
        {
            ind = i - 1;
            break;
        }
    }
    return ind;
}

int main()
{
    string file_name = "B-large";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        string n;
        f1 >> n;
        while(is_tidy(n) >= 0)
        {
            int ind = is_tidy(n);
            n[ind] = n[ind] - 1;
            for(int i = ind+1; i <= n.size(); ++i)
            {
                n[i] = '9';
            }
        }
        bool zeros = 1;
        for(int i = 0; i < n.size(); ++i)
        {
            if(n[i] != '0')
            {
                zeros = 0;
            }
            if(n[i] != '0')
            {
                f2 << n[i];
            }
            if(n[i] == '0' && !zeros)
            {
                f2 << n[i];
            }
        }
        f2 << endl;
        //f2 << n << endl;
    }
    return 0;
}

