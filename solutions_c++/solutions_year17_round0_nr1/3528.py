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

int tests, k, ans = 0;
string s;
void sw(char &c){
    if(c == '+') c = '-';
    else c = '+';
}
bool ok(string &s){
    for(auto c : s){
        if(c == '-') return 0;
    }
    return 1;
}
int solve1(string s, int k){
    int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int ans = INF;
    do{
        string t = s;
        int res = 0;
        for(auto i : a){
            if(ok(t))break;
            if(i + k - 1 >= t.size())continue;
            res++;
            for(int j = 0; j < k; j++){
                sw(t[i+j]);
            }
        }
        if(ok(t)) ans = res;
    }while(next_permutation(a, a+s.size()));
    if(ans == INF) ans = -1;
    return ans;
}
int main ()
{
    srand(time(0));
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin >> tests;
    for(int test = 1; test <= tests; test++){
        cerr<<test<<"\n";
        ans = 0;
        cin>>s>>k;
//        int ans1 = solve1(s, k);
        for(int i = 0; i < s.size() - k + 1; i++){
            if(s[i] == '-'){
                ans++;
                for(int j = 0; j < k; j++){
                    sw(s[i+j]);
                }
            }
        }
        if(!ok(s))ans = -1;
        cout<<"Case #"<<test<<": ";
        if(ans == -1)cout<<"IMPOSSIBLE\n";
        else cout<<ans<<"\n";
    }
    return 0;
}
