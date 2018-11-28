//
//  main.cpp
//  q2
//
//  Created by Ken-Hao Liu on 09/04/2017.
//  Copyright © 2017 Ken-Hao Liu. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution{
public:
    string solve(string &s){
        string result=s;
        for(int i=0;i+1<s.size();i++){
            if(s[i]>s[i+1]){
                while(i>0&&s[i-1]==s[i])i--;
                getPrev(result,i);
                break;
            }
        }
        return result;
    }
    void getPrev(string &result, int pos){
        result[pos]--;
        for(int i=pos+1;i<result.size();i++)result[i]='9';
        if(!pos&&result[0]=='0')result=result.substr(1);
    }
};
int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        string s,result;
        cin>>s;
        Solution sol;
        result=sol.solve(s);
        printf("Case #%d: %s\n",i+1,result.c_str());
    }
    return 0;
}
