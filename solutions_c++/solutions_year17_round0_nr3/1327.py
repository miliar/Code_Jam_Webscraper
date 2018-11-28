//
//  main.cpp
//  codejam_2016
//
//  Created by fchowdhu on 4/9/16.
//  Copyright © 2016 fchowdhu. All rights reserved.
//

#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<set>
#include<fstream>
#include<cfloat>
#include<cassert>
using namespace std;

typedef long long  LL;
typedef vector<int>   vi;
typedef pair<int,int>  pii;


long long f[200000];
long long s[200000];
long long arr[200000];
long long vis[200000];
#define MOD 1000000009
long long bm(long long a, long long p){
    if(p==0)return 1;
    else if(p%2==0){
        long long x = bm(a,p/2);
        x*=x;
        x%=MOD;
        return x;
    }else{
        long long x = bm(a,p-1);
        x*=a;
        x%=MOD;
        return x;
    }
}
long long ncr(long long n, long long r){
    
    long long ans = f[n];
    ans *= bm(f[n-r],MOD-2);
    ans%=MOD;
    ans *= bm(f[r],MOD-2);
    ans%=MOD;
   // cout<<n<<"--"<<r<<"--"<<ans<<endl;
    return ans;
}


int main() {
    int C=0;
    freopen("/Users/fchowdhu/Downloads/C-large.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/C-large.out", "w", stdout);
    int t, cn = 1;
    cin>>t;
    while(t--){
        long long n,k;
        cin>>n>>k;
        map<long long, long long > mp;
        mp[-n] = 1;
        long long c=0;
        cout<<"Case #"<<cn++<<": ";
        for (auto i = mp.begin(); i!=mp.end(); i++) {
            long long x = -i->first;
            c+=i->second;
            if(c>=k){
                cout<<x/2<<" "<<x-x/2-1<<endl;
                break;
            }
            mp[-x/2] += i->second;
            mp[-(x-1-x/2)] += i->second;
        }
        
        
    }
    
    return 0;
}
