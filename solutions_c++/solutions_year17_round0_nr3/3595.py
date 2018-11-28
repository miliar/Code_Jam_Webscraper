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


int tests;
ll n, k;
multiset<ll> s;
int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin >> tests;
    for(int test = 1; test <= tests; test++){
        cerr<<test<<"\n";
        cin>>n>>k;
        s.clear();
        s.insert(-n);
        int a = 0, b = 0;
        for(int i=1; i<=k; i++){
            int now = *s.begin();
            if(now == 0)continue;
            now++;
            s.erase(s.begin());
            s.insert(a = now/2);
            s.insert(b = now/2 + now%2);
        }
        cout<<"Case #"<<test<<": ";
        cout<<-b<<" "<<-a<<"\n";
    }
    
    return 0;
}
