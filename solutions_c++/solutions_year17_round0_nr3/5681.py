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

typedef long long int lli;

using namespace std;

int main()
{
    ifstream in("/Users/Rajdeep/Downloads/Google Code Jam Practice/Google Code Jam Practice/C-small-1-attempt0.in");
    ofstream out("/Users/Rajdeep/Downloads/Google Code Jam Practice/Google Code Jam Practice/output.txt");
    int t;
    in>>t;
    for(int az=1;az<=t;az++)
    {
        lli n,ma;
        in>>n;
        lli k;
        in>>k;
        vector<lli> v,o,ls,rs,yu,yr,yl;
        v.push_back(0);
        v.push_back(n+1);
        for(lli i=1;i<=k;i++)
        {
            sort(v.begin(),v.end());
            
            ma =0;
            for(lli j =0 ;j<v.size()-1; j++)
            {
                lli u;
                u = v[j]+v[j+1];
                u=u/2;
                if(ma<min(u-v[j],v[j+1]-u))
                {
                    ma = min(u-v[j],v[j+1]-u);
                    o.clear();
                    ls.clear();
                    rs.clear();
                    o.push_back(u);
                    ls.push_back(u-v[j]);
                    rs.push_back(v[j+1]-u);
                }
                else if(ma == min(u-v[j],v[j+1]-u))
                {
                    o.push_back(u);
                    ls.push_back(u-v[j]);
                    rs.push_back(v[j+1]-u);
                }
            }
            ma = 0;
            for(lli j =0 ; j<o.size();j++)
            {
                if(ma<max(ls[j],rs[j]))
                {
                    ma = max(ls[j],rs[j]);
                    yu.clear();
                    yr.clear();
                    yl.clear();
                    yu.push_back(o[j]);
                    yl.push_back(ls[j]);
                    yr.push_back(rs[j]);
                }
                else if(ma == max(ls[j],rs[j]))
                {
                    yu.push_back(o[j]);
                    yl.push_back(ls[j]);
                    yr.push_back(rs[j]);
                }
            }
            if(i==k)
            {
                out<<"Case #"<<az<<": "<<max(yl[0]-1,yr[0]-1)<<" "<<min(yl[0]-1,yr[0]-1)<<endl;
            }
            else
            {
                v.push_back(yu[0]);
            }
        }
    }
    return 0;
}