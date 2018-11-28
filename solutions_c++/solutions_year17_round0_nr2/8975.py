#include <iostream>

using namespace std;

typedef long long ll;

int main() {
    ll t;
    cin>>t;
    for(ll c = 1 ; c <= t; c++) {
        ll n;
        cin>>n;
        bool s = false;
        do {
            ll k = n;
            ll prev = 10;
            bool S = true;
            while(k) {
                ll d = k % 10;
                k /= 10;
                if(prev < d) {
                    S = false;
                    break;
                }
                prev = d;
            }
            s = S;
        } while(!s && --n);
        cout<<"Case #"<<c<<": "<<n<<endl;
    }
    return 0;
}