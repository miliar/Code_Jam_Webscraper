//
//  main.cpp
//  gcj_qual_b
//
//  Created by yupeng gou on 4/7/17.
//  Copyright © 2017 yupeng gou. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>


using namespace std;

bool judge(string s){
    for(int i = 0 ; i + 1 < s.length() ; i++){
        if(s[i] > s[i + 1])
            return false;
    }
    return true;
}
string construct(string s,int limit ,bool start){
    if(s == "") return "";
    
    int cur = s[0] - '0';
    if (cur >= limit){
        char c = '0' + cur;
        string tail = construct(s.substr(1,s.length()-1), max(cur,limit),false);
        if(tail != "")
            return c + tail;
        else{
            cur--;
        }
    }
//    cout<<s<<' '<<limit<<endl;
    if(cur == 0){;
       return "";
    }else{
        string ans(s.length() - 1 ,'9');
        if(ans == "" || (!start && cur < limit)) return "";
        char tmp = '0' + cur;
        return tmp + ans;
    }
    
}

string cal(string s){
    if(judge(s))
        return s;
    else{
        string tmp = construct(s , s[0] - '0' ,true);
        if(tmp == ""){
            string ans(s.length() - 1 , '9');
            return ans;
        }else
            return tmp;
    }
}

int main(int argc, const char * argv[]) {
    freopen("/Users/yupenggou/Documents/gcj_2016_practice/gcj_qual_b/in.txt" , "r" , stdin);
    freopen("/Users/yupenggou/Documents/gcj_2016_practice/gcj_qual_b/out.txt" , "w" , stdout);
    int cases;
    cin >> cases;
    for(int it = 1 ; it <= cases; it++){
        string s;
        cin >> s;
        cout<<"Case #"<<it<<": "<<cal(s)<<endl;
    }
    return 0;
}
/*
1
320
7
111111111111111110
99999999999999999
99999999999999999
 */
