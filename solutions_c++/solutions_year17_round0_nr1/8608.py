//
//  main.cpp
//  practice2
//
//  Created by Rajdeep Singh Dhingra on 10/06/16.
//  Copyright © 2016 Rajdeep Singh Dhingra. All rights reserved.
//

#include <iostream>
#include <set>
#include <vector>
#include <fstream>
using namespace std;

typedef set<int>::iterator ite;

int main()
{
    ifstream in("/Users/Rajdeep/Downloads/practice2/practice2/input.txt");
    ofstream out("/Users/Rajdeep/Downloads/practice2/practice2/output.txt");
    int n,rank;
    in>>n;
    set<int> s;
    for(int i=0;i<n;i++)
    {
        int y;
        in>>y;
        s.insert(y);
    }
    int m;
    in>>m;
    for(int i=0;i<m;i++)
    {
        int y;
        in>>y;
        s.insert(y);
        ite it;
        rank = 0;
        for(it = s.begin();it!=s.end();it++)
        {
            rank++;
            if(*it==y)
            {
                out<<s.size()-rank+1<<endl;
                s.erase(s.begin(),it);
                break;
            }
        }
    }
    return 0;
}