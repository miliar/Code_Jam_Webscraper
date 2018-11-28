//
//  main.cpp
//  codejam01
//
//  Created by Ray Xu on 8/04/2017.
//  Copyright © 2017 Ray Xu. All rights reserved.
//

#define FILEINPUT 1

#include <iostream>
#include <vector>
using namespace std;

int flip(vector<char> &pan, int beg, int k)
{
    int pos = -1;
    for (int i = beg; i < beg+k; i++)
    {
        if (pan[i]=='-')
            pan[i]='+';
        else
        {
            pan[i]='-';
            if (pos == -1)
                pos = i;
        }
        
    }
    if (pos!=-1)
        return pos;
    else
        return beg+k;
}

int solve( vector<char> &pan, int k)
{
    int ans=0;
    int i=0;
    for (; i <=pan.size()-k;)
    {
        if (pan[i]=='-'){
            i = flip(pan, i, k);
                ans++;
        }else
            i++;
    }

    for (auto m: pan){
        if (m=='-')
            return -1;
    }
    return ans;
}


int main(int argc, char **argv) {
    int t;
    if (argc>1) {
        freopen(argv[1], "r", stdin);
    }
    
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    vector<char> pancakes;
    for (int i = 1; i <= t; ++i) {
        char in;
        int answer = -1;
        cin >> in;
        int k;
        while (true) {
            if (in == '+' || in == '-')
                pancakes.push_back(in);
            else if (isspace(in))
            {
                cin>>skipws>>k;
                break;
            }
            cin>>noskipws>>in;
        }
        answer = solve (pancakes, k);
        pancakes.clear();
        if (answer>=0)
            cout << "Case #" << i<<": "<<answer << endl;
        else
            cout << "Case #" << i<<": "<<"IMPOSSIBLE"<< endl;
        
    }
}
