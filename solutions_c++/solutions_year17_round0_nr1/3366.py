//
// Created by Snehil Vishwakarma on 4/7/17.
//
// Oversized Pancake Flipper

#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <string>
#include <numeric>

using namespace std;

int main() {
    int T,k,pos,ct;
    string s;
    bool chk,fchk;

    cin>>T;
    for(int i=0; i<T; ++i)
    {
        cin >> s >> k;
        ct = 0;
        chk = true;
        while (chk)
        {
            chk = false;
            fchk = true;
            for (pos = 0; pos < s.length(); ++pos)
            {
                if (s[pos] == '-')
                {
                    fchk = false;
                    if (pos + k - 1 >= s.length())
                        break;
                    else
                    {
                        chk = true;
                        ct++;
                        for (int j=pos; j < pos+k; ++j)
                        {
                            if (s[j] == '+')
                                s[j] = '-';
                            else
                                s[j] = '+';
                        }
                    }
                }
            }
        }
        if (fchk)
            cout << "Case #" << (i + 1) << ": " << ct;
        else
            cout << "Case #" << (i + 1) << ": IMPOSSIBLE";
        if(i!=(T-1))
            cout << endl;
    }
    return 0;
}