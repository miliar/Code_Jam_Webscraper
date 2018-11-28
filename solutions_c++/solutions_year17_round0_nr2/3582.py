#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<ll> tidy;


void gen(int i, int len, ll x){

    if(i > 9){
        if(x != 0)tidy.push_back(x);
        return;
    }

    ll y = x;
    for(int j = len; j < 18; ++j){
        y = y*10 + i;
        gen(i+1, j+1, y);
    }

    gen(i+1,len,  x);

}


int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("oneB.txt", "w", stdout);
    gen(1, 0, 0);
    sort(tidy.begin(), tidy.end());
   // cout << tidy[0];
    /*for(int i = 0; i < 50; ++i){
        cout  << tidy[i] << endl;
    }*/
    int t; cin >> t;
    for(int z = 1; z <= t; ++z){
        ll tmp;
        cin >> tmp;
        int ans = lower_bound (tidy.begin(), tidy.end(), tmp) - tidy.begin();
        if(tidy[ans] == tmp)printf("Case #%d: %lld\n", z, tidy[ans]);
        else printf("Case #%d: %lld\n", z, tidy[ans-1]);
    }
}

