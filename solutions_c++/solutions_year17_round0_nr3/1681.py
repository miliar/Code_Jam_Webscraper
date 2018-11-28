#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
map<ll,ll> mp;
int main()
{
    ifstream cin("C-large.in");
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    for(int tc=1 ;  tc<=t; tc++){
        ll n , k ;
        cin >> n >> k ;
        priority_queue<ll> q ;
        q.push(n);
        k;
        mp.clear();
        mp[n]++;
        ll ans1=0 ,ans2=0 ;
        while(k){
            map<ll,ll>::iterator it = mp.end();
            it--;
            ll kk = it->second ;
            ll nn = it->first;
            mp.erase(it);
//            cout << nn <<  ' ' << kk <<endl;
            nn-- ;
            kk = min(kk,k);
            k-=kk;
            ll a = nn/2 ;
            ll b = nn/2 + (nn&1);
            ans1= b ;
            ans2 = a;

            mp[a]+=kk ;
            mp[b]+=kk;
        }

        cout << "Case #" << tc << ": "<<ans1 << ' ' <<ans2<<endl;

    }
}
