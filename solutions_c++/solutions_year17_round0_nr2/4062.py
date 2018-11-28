#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1e14;

long long power(long long a, long long n){
    long long ans = 1;
    for (; n; n >>= 1, a = a * a)
        if (n & 1) ans = ans * a;
    return ans;
}

 int main(){
    int T;
    cin >> T;
    for(ll i = 1; i <= T; i++){
        string x; cin >> x;
        cout << "Case #" << i << ": ";
        ll lastpos = int(x.size());
        ll lastnum = int (x[x.size()-1]);
        for(ll j = int(x.size()) - 2; j >= 0; j--){
            if(int(x[j]) > lastnum){
                lastpos = j;
                lastnum = int(x[j]);
                lastnum --;
            }
            else lastnum = int(x[j]);
        }
        for(ll j = x.size()-1; j >= 0; j--){
            if(j > lastpos) x[j] = '9';
            else if(j == lastpos) x[j] = char(int(x[j]) - 1);
        }
        ll ans = 0;
        for(ll j = 0; j < x.size(); j++){
            ll p = int(x.size()) - 1;
            ll num = int(x[j]) - 48;
            ans += num*power(10, p-j);
        }
        cout << ans << endl;
    }
 }
