//
//  main.cpp
//  gcj_qual_a
//
//  Created by yupeng gou on 4/7/17.
//  Copyright © 2017 yupeng gou. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;


int get_step(string cake, int len){
    int n = cake.length();
    int status[10005];
    memset(status, 0, sizeof status);
    int ans = 0;
    for(int i = 0 ; i < cake.length() ; i++){
//        cout<<i<<' '<<status[i]<<endl;
        bool cur = cake[i] == '+' ? true : false;
        if(i!= 0)
            status[i] += status[i - 1];
//        cout<<status[i]<<' '<<cake[i]<<endl;
        bool flip = status[i] % 2 == 0 ? true : false;
        if(cur == flip){
            continue;
        }else{
            if(i + len > n)
                return -1;
            ans++;
            status[i] += 1;
            if(i + len < n)
                status[i + len] += -1;
        }
//        cout<<i<<' '<<ans<<' '<<status[i]<<endl;
        
    }
//    cout<<ans<<endl;
    return ans;
}


using namespace std;
int main(int argc, const char * argv[]) {
    freopen("/Users/yupenggou/Documents/gcj_2016_practice/gcj_qual_a/in.txt", "r", stdin);
    freopen("/Users/yupenggou/Documents/gcj_2016_practice/gcj_qual_a/out.txt", "w", stdout);
    int num_case;
    cin >> num_case;
    for(int it = 1 ; it <= num_case ; it++){
        string cake;
        int len;
        cin >> cake >> len;
        int ans = get_step(cake ,len);
        if (ans >= 0)
            cout <<"Case #"<<it<<": "<<ans<<endl;
        else
            cout <<"Case #"<<it<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
