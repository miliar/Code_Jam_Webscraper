//
//  main.cpp
//  atcoder
//
//  Created by IshikawaTakumi on 2016/05/28.
//  Copyright © 2016年 IshikawaTakumi. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <set>
#include <functional>
#include <map>
#include <queue>
#include <cstring>
#include <stack>
#include <iomanip>
#include <climits>
#include <numeric>
using namespace std;
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define show(x) cout << #x << " = " << x << endl;
typedef long long ll;
typedef pair<int,int> P;
int check(ll n){
    string s = to_string(n);
    rep(i,s.size()-1){
        if(s[i]>s[i+1]){
            return i;
        }
    }
    return -1;
}
bool check2(ll n){
    string s = to_string(n);
    string a,b;
    rep(i,s.size()-1){
        a+="9";
        b+="1";
    }
    b+="0";
    if(stoll(a)<n&&n<=stoll(b)){
        return true;
    }else{
        return false;
    }
}
int main(){
    int t;
    cin >> t;
    for(int test = 1; test <= t; test ++){
        cout << "Case #" << test << ": ";
        ll n;
        cin >> n;
        if(check(n)==-1){
            cout << n << endl;
            continue;
        }
        if(check2(n)){
            string s = to_string(n);
            rep(i,s.size()-1){
                cout << 9;
            }
            cout << endl;
            continue;
        }
        while(1){
            int k = check(n);
            if(k==-1)break;
            //show(k);
            string s = to_string(n);
            int h = s[k]-'0';
            //show(h);
            h--;
            s[k] = (char)('0'+h);
            for(int i = k+1;i<s.size();i++){
                s[i] = '9';
            }
            n = stoll(s);
        }
        cout << n << endl;
    }
}
