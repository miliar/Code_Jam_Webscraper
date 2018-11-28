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
void solv(ll n,ll k){
    //cout << "n = " << n << " "<<  "k = " << k << endl;
    if(k==1){
        cout << n/2 << " " << (n-1)/2 << endl;
    }
    else if(n%2==1){
       solv(n/2,k/2);
    }else{
        if(k==2){
            solv(n/2,1);
        }
        else if(k%2==0){
            solv(n/2,k/2);
        }else{
            solv(n/2-1,(k-1)/2);
        }
    }
}
int main(){
    int t;
    cin >> t;
    for(int test = 1; test <= t; test ++){
        cout << "Case #" << test << ": ";
        ll n,k;
        cin >> n >> k;
        solv(n,k);
    }
}
