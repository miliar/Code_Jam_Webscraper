//
// Created by Snehil Vishwakarma on 4/7/17.
//
// Tidy Numbers

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
    int T,pos,k;
    string s;
    cin>>T;
    for(int i=0; i<T; ++i)
    {
        cin>>s;
        for(int j=0; j<(s.length()-1); ++j)
        {
            pos=j;
            while(j<(s.length()-1))
            {
                if(s[j]!=s[j+1])
                    break;
                ++j;
            }
            if(j==(s.length()-1))
                break;
            if(s[j] > s[j+1])
            {
                for(k=j; k>pos && k>0; --k)
                    s[k]=57;
                --(s[k]);
                ++j;
                for(; j<s.length(); ++j)
                    s[j]=57;
            }
        }
        if(s.length() == 1)
            cout << "Case #" << (i+1) << ": " << s;
        else if(s[0] == 48)
            cout << "Case #" << (i+1) << ": " << s.substr(1);
        else
            cout << "Case #" << (i+1) << ": " << s;
        if(i!=(T-1))
            cout << endl;
    }
    return 0;
}