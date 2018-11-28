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

void solv(int r,int c){
    vector<string>a(r);
    rep(i,r){
        cin >> a[i];
        rep(j,c){
            if(a[i][j]!='?'){
                char k = a[i][j];
                int p = j+1;
                while(p<c && a[i][p]=='?'){
                    a[i][p] = k;
                    p++;
                }
                p = j-1;
                while(p>=0 && a[i][p] == '?'){
                    a[i][p] = k;
                    p--;
                }
            }
        }
    }
    rep(i,r){
        bool flag = false;;
        rep(j,c){
            if(a[i][j]!='?')flag = true;
        }
        if(flag == false && i!=r-1){
            int k = i+1;
            while(1){
                if(a[k][0]!='?' || k >=r)break;
                else k++;
            }
            if(k==r){
                k = i-1;
                while(1){
                    if(a[k][0]!='?')break;
                    else k--;
                }
            }
            a[i] = a[k];
        }
        if(flag == false && i==r-1){
            a[i] = a[i-1];
        }
    }
    rep(i,r){
        cout << a[i] << endl;
    }
    
}
int main(){
    int t;
    cin >> t;
    for(int test = 1; test <= t; test ++){
        cout << "Case #" << test << ":" << endl;
        int r,c;
        cin >> r >> c;
        solv(r,c);
    }
}
