//
//  main.cpp
//  code
//
//  Created by ravi kumar on 09/02/17.
//  Copyright © 2017 code. All rights reserved.
//

#include <iostream>
#include <set>
#include <utility>

using namespace std;

long long int a[1000006], d[1000006];

long long int b[1000006], e[1000006];

long long int c[1000006], f[1000006];

string s;
long long n;

set< pair< long long, long long > > meraset;

long long solve(){
    long long l = s.length();
    long long ans = 0;
    long long add = 0;
    
    for( int i = 0; i < l; i++ ){
        a[i] = 0;
    }
    
    for( int i = 0; i < l; i++ ){
        if( (s[i]-'0'+add)%2 == 0 ){
            a[i] = 1;
        }else{
            a[i] = 0;
        }
        if( i >= n-1 ){
            add += a[i] - a[i-n+1];
        }else{
            add += a[i];
        }
        
        if( i>l-n && a[i]==1)return -2;
        
        ans += a[i];
    }
    return ans;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    long long t;
    cin>>t;
    for( int T = 1; T <= t; T++ ){
        cin>>s>>n;
        
        for( int i = 0; i < s.length();i++ ){
            if( s[i] == '+')s[i] = '1';
            else s[i] = '0';
        }
        long long AAA = solve();
        cout<<"Case #"<<T<<": ";
        if( AAA != -2 ){
            cout<<AAA<<endl;
        }else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
    
    return 0;
}


/*
 1 2
 1 3
 2 3
 
 1 2 3 4
 1-4, 1=2 2=3 3=4
 3
 ---+-++- 3
 +++++ 4
 -+-+- 4
*/
