#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define ll long long

pair<ll, ll> get(ll num){
    pair<ll, ll> res;
    if(num % 2){
        res.first = num/2;
        res.second = res.first;
    }
    else{
        res.first = num/2 - 1;
        res.second = num/2;
    }

    if(res.first < res.second)
        swap(res.first, res.second);

    return res;
}

int main(){

    freopen("C-large.in", "r", stdin);
    freopen("output7.txt", "w", stdout);
    int tt;
    cin>>tt;

    for(int ttt = 1; ttt <= tt; ttt++){
        ll n, k;
        cin>>n>>k;

        ll level = 1;
        ll curr_n = n;

        ll used = 0;
        while((used + level) < k){
            used += level;
            curr_n -= level;
            level *= 2;
        }

        ll a = curr_n % level;

        ll b = k - used;
        ll res = (curr_n / level);
        if(b <= a){
            res++;
        }

        pair<ll, ll> t = get(res);
        cout<<"Case #"<<ttt<<": "<<t.first<<" "<<t.second<<endl;
    }

    return 0;
}
