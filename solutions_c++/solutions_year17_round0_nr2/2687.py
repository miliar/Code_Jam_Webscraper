#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

ll f(ll x){
    vector<int> a;
    while(x){
        a.pb(x % 10);
        x /= 10;
    }
    reverse(all(a));
    int n = a.size();

    ll ans = 0;
    for(int i = 0; i < n - 1; i++){
        ans = ans * 10 + 9;
    }

    int p = 0, l = -1;
    ll cur = 0;
    for(int i = 0; i < n; i++){
        if(p > a[i]){
            if(l == -1){
                return ans;
            }

            while(i > l){
                i--;
                cur /= 10;
            }
            cur = cur * 10 + (a[i] - 1);
            for(int j = i + 1; j < n; j++){
                cur = cur * 10 + 9;
            }
            return cur;
        }
        if(a[i] > p){
            l = i;
        }
        p = a[i];
        cur = cur * 10 + a[i];
    }
    return cur;
}


int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int num = 1; num <= T; num++){
        cout << "Case #" << num << ": ";
        ll n;
        cin >> n;
        cout << f(n) << "\n";
    }
}
