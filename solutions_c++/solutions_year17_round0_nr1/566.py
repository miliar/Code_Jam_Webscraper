//
//  main.cpp
//  qr
//
//  Created by Ran Wang on 4/7/17.
//  Copyright © 2017 Ran Wang. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

char flip(char c)
{
    return c == '-' ? '+' : '-';
}

int main(int argc, const char * argv[]) {
    int T, k;
    string s;
    cin >> T;
    
    for(int caset = 1; caset <= T; caset++)
    {
        int res = 0;
        cin >> s >> k;
        
        // greedy
        int pos = 0;
        while(pos < s.size())
        {
            if(s[pos] == '+')
            {
                pos++;
                continue;
            }
            else
            {
                if(pos + k > s.size())
                    break;
                res++;
                for(int i = pos; i < pos + k; i++)
                    s[i] = flip(s[i]);
            }
        }
        
        cout << "Case #" << caset << ": " <<
        (pos < s.size() ? "IMPOSSIBLE" : to_string(res)) << endl;
    }
}
