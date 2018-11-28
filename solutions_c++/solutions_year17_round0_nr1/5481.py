//
//  main.cpp
//  Google Code Jam Practice
//
//  Created by Rajdeep Singh Dhingra on 20/03/17.
//  Copyright © 2017 Rajdeep Singh Dhingra. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("/Users/Rajdeep/Downloads/Google Code Jam Practice/Google Code Jam Practice/A-large.in");
    ofstream out("/Users/Rajdeep/Downloads/practice2/practice2/output.txt");
    int t;
    in>>t;
    for(int az=1;az<=t;az++)
    {
        string s;
        in>>s;
        int k;
        int n=0;
        in>>k;
        string a,b;
        a = "+";
        b = "-";
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                if (i+k<=s.length())
                {
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                    n++;
                }
                else
                {
                    out<<"Case #"<<az<<": IMPOSSIBLE"<<endl;
                    break;
                }
            }
        }
        size_t found = s.find(b);
        if(found==string::npos)
        {
            out<<"Case #"<<az<<": "<<n<<endl;
        }
    }
    return 0;
}