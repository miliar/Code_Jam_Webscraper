//
//  main.cpp
//  problem B
//
//  Created by Twinkle Gupta on 4/7/17.
//  Copyright © 2017 Twinkle Gupta. All rights reserved.
//

#include <iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

bool check(string s)
{
    
    for (int i = 1; s[i] != '\0'; i++) {
        
        if(s[i] < s[i-1]) return false;
    }
    return true;
}


int main() {
    int t;
    cin>>t;
    for(int i = 1; i<=t; i++){
        string s,ans;
        cin>>s;
        if(check(s)) ans = s;
        else{
            int n = s.length();
            for(int j = n-1; j > 0;j--)
            {
                if(s[j] < s[j-1]){
                    for(int k = j; k < n; k++) s[k] = '9';
                    s[j-1]--;
                }
            }
            ans = s.erase(0, min(s.find_first_not_of('0'), s.size()-1));
            
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
        
    }
       return 0;
}
