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
string tidyUp(string n){
    for (int i=n.size()-2; i>=0; i--) {
        if(n[i]>n[i+1]){
            for (int j=i+1; j<n.size(); j++) {
                n[j] = '9';
            }
            n[i] = n[i]-1;
        }
       // cout<<n<<endl;
    }
    int i = 0;
    while (i<n.size() && n[i]=='0') {
        n.erase(i,1);
    }
    return n;
}
int main() {
    int C=0;
    freopen("/Users/fchowdhu/Downloads/B-large.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/B-large.out", "w", stdout);
    int t, cn = 1;
    cin>>t;
    while(t--){
        int n;
        string str, str1;
        cin>>str;
        cout<<"Case #"<<cn++<<": "<<tidyUp(str)<<endl;
        
    }
    
    return 0;
}
