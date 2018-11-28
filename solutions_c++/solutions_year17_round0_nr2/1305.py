//
//  main.cpp
//  google cj1 q
//
//  Created by Magen on 08/04/2017.
//  Copyright © 2017 Magen. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin>>T;
    bool first=true;
    for(int i=1;i<=T;i++)
    {
        if(first)first=false;
        else cout<<endl;
        string s;
        cin>>s;
        for(int j=s.size()-2;j>=0;j--)
        {
            if(s[j]<=s[j+1])continue;
            if(s[j]=='0')continue;
            s[j]--;
            for(int k=j+1;k<s.size();k++)
                s[k]='9';
        }
        if(s[0]=='0')s.erase(s.begin());
        cout<<"Case #"<<i<<": "<<s;
        
    
    }
    return 0;
}
