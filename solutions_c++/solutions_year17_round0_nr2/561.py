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
        cin >> s;
        
        string res;
        
        int i = 0;
        
        for(; i < s.size() - 1; i++)
        {
            if(s[i] > s[i+1])
            {
                break;
            }
        }
        
        
            
        if(i >= s.size() - 1)res = s;
        else
        {
            while(i > 0 && s[i] == s[i-1])i--;
            long long num = stoll(s.substr(0, i+1));
            num--;
            res = (num == 0 ? "" : to_string(num)) + string(s.size() - i - 1, '9');
        }
        
        cout << "Case #" << caset << ": " << res << endl;
    }
}
