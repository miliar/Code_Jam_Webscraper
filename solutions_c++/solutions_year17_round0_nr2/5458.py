//
//  main.cpp
//  HackerEarth Practice
//
//  Created by Rajdeep Singh Dhingra on 03/04/17.
//  Copyright © 2017 Rajdeep Singh Dhingra. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

typedef long long int lli;

using namespace std;

int main()
{
    ifstream in("/Users/Rajdeep/Downloads/Google Code Jam Practice/Google Code Jam Practice/B-large.in");
    ofstream out("/Users/Rajdeep/Downloads/Google Code Jam Practice/Google Code Jam Practice/output.txt");
    int t;
    in>>t;
    for(int az=1;az<=t;az++)
    {
        string s;
        in>>s;
        char a;
        int l;
        vector<int> v;
        for(int i=0;i<s.length();i++)
        {
            a = s[i];
            l = a - '0';
            v.push_back(l);
        }
        for(int i=0;i<v.size()-1;i++)
        {
            if(v[i]>v[i+1])
            {
                v[i]--;
                for(int j=i+1;j<v.size();j++)
                    v[j]=9;
                if(v[i-1]>v[i])
                {
                    i= i-2;
                }
                else
                    break;
            }
        }
        out<<"Case #"<<az<<": ";
        for(int i=0;i<v.size();i++)
        {
            if(v[0]==0 && i == 0)
            {
                s = "gaba";
            }
            else
                out<<v[i];
        }
        out<<endl;
    }
    return 0;
}