#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
#define INFL 0x3f3f3f3f3f3f3f3fLL
const int mod = 1e9+7;

const int M = 100001;


double pi = 3.141592653589793238462643;
int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T;
    si(T);

    for(int alp = 1 ; alp <= T ; alp++){
       // int ans = 0;

        int n , k;
        si(n);  si(k);
       // reset(n , k);

        vector<pair<ll , ll> > vec;



        for(int i = 1 ; i <= n ; i++){
            ll r , h;
            sll(r);  sll(h);
            vec.push_back(make_pair(r , h));
        }

        sort(vec.begin() , vec.end());
        ll ans = 0;

        while(vec.size() >= k){
        ll rad = vec.back().first;
        ll he  = vec.back().second;
        ll t_ans = 0;
        t_ans = rad*1LL*rad + 2*rad*1LL*he;

        vec.pop_back();
        vector<ll> vv;
        for(int i = 0 ; i < vec.size() ; i++){
            ll r = vec[i].first;
            ll h = vec[i].second;
            vv.push_back(r*(h*1LL));
        }
        sort(vv.begin() , vv.end());

        int pic = 0;
        for(int i = vv.size() - 1 ; i >= 0 ; i--){
            if(pic == k - 1) break;
            pic++;
            t_ans += (2*vv[i]);
        }
        ans = max(ans , t_ans);
        }
        double how = ans*pi;

        printf("Case #%d: " , alp);
        printf("%.10f\n" , how);

    }

}
