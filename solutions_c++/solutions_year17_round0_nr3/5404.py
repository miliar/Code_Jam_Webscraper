#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define s(x) scanf("%lld" , &x)

int main()
{
    freopen("cs.txt" , "r" , stdin);
    freopen("ocs.txt" , "w" , stdout);
    ll t , p = 0;
    s(t);
    while(t--){
        p ++;
        ll n , k , i , mx;
        cin >> n >> k;
        multiset<ll> s;
        s.insert(n);
        //set<ll> :: iterator it;
        for(i = 1; i < k; i ++){
            mx = *s.rbegin();
            if(mx&1){
                s.insert(mx/2);
                s.insert(mx/2);
            }
            else{
                s.insert(mx/2);
                s.insert(mx/2-1);
            }
            s.erase(--s.end());
        }
        mx = *s.rbegin();
        cout << "Case #" << p << ": ";
        if(mx&1){
            cout << mx/2 << " " << mx/2;
        }
        else{
            cout << mx/2 << " " << mx/2-1;
         }
         cout << endl;
    }
    return 0;
}
