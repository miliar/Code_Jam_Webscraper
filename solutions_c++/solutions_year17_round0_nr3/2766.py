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

map<ll, ll> f;

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int num = 1; num <= T; num++){
        cout << "Case #" << num << ": ";
        ll n, k;
        cin >> n >> k;

        f[-n] = 1;
        ll d = 0;
        while(k > 0){
            if(f.empty()){
                cout << "lol";
                break;
            }
            pair<ll, ll> x = *f.begin();
            f.erase(f.begin());

            x.x = -x.x;
            //cout << x.y << "\n";
            if(k > x.y){
                k -= x.y;
                if(x.x > 1){
                    if(x.x % 2){
                        f[-(x.x / 2)] += 2 * x.y;
                    } else {
                        f[-(x.x / 2)] += x.y;
                        if(x.x > 3)f[-(x.x / 2 - 1)] += x.y;
                    }
                }
            } else {
                d = x.x;
                break;
            }
        }

        if(d % 2){
            cout << d / 2 << " " << d / 2 << "\n";
        } else {
            cout << d / 2 << " " << d / 2 - 1 << "\n";
        }
        f.clear();
    }
}
