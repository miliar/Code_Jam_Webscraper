/*
 Created by Saidolda Bayan.
 Copyright (c) 2015 Bayan. All rights reserved.
 LANG: C++
 */
#include <bits/stdc++.h>

#define _USE_MATH_DEFINES
#define y1 lalka
#define right napravo
#define left nalevo
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
using pii = pair<int, int>;
using ll = long long;

const int INF = (int)1e9+7, mod = (int)1e9+9, pw = 31, N = (int)1e5+123, M = (int)1e6+123;
const double eps = 1e-11;
const long long inf = 1e18;

bool tidy(ll x){
    int last = 9;
    while(x){
        if(x % 10 > last)return 0;
        last = x % 10;
        x /= 10;
    }
    return 1;
}

int tests;
ll n;

int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin >> tests;
    for(int test = 1; test <= tests; test++){
                cerr<<test<<"\n";
        cin>>n;
        //        int m = n;
        //        while(!tidy(m))m--;
        cout<<"Case #"<<test<<": ";
        string s = to_string(n);
        for(int j=1; j<=20; j++){
            bool change = 0;
            for(int i = 0; i < s.size(); i++){
                if(change){
                    s[i] = '9';
                }
                else{
                    if(i+1 < s.size() && s[i] > s[i+1]){
                        s[i]--;
                        change = 1;
                    }
                }
            }
            if(s[0] == '0')s.erase(s.begin());
        }
        cout<<s<<"\n";
    }
    
    return 0;
}
