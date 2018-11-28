
#include <iostream>
using namespace std;

typedef long long ll;
bool check(ll n){
    int tmp = 10;
    int x;
    ll nn = n;
    while(nn > 0){
        x = nn%10;
        //cout << nn << ", " << x << ", " << tmp << endl;
        if (x > tmp) return false;
        nn = nn/10;
        tmp = x;
    }
    return true;
}
int main() {
    freopen("B-large.in", "r", stdin);
    	freopen("ans.txt", "w", stdout);
    
    int t;
    cin >> t;
    ll s;
    for (int it = 1; it <= t; ++it) {
        cout<<"Case #"<<it<<": ";
        cin>>s;
        ll cnt = 0;
        for(ll i=s;i>=1;i--) {
            if (check(i)){
                cnt = i;
                break;
            }
        }
        cout << cnt << "\n";
    }

    return 0;
}
