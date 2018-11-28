#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#define ll long long
#define n J.size()
//#define sort(A) sort(A.begin(),A.end())
//#define rsort(A) sort(A.rbegin(),A.rend())
using namespace std;
static const ll D = 1000000007;
static const double PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

int main() {
    ll T, ac, aj, c, d;
    ll ti[2], m[2], j[2];
    cin >> T;
    for(ll t = 0; t<T; ++t){
        cin >> ac >> aj;
        ti[0] = ti[1] = 720;
        vector<pair<pair<ll, ll>, ll> > J(ac+aj);
        for(ll i = 0; i<ac; ++i){
            cin >> c >> d;
            J[i] = make_pair(make_pair(c, d), 0);
            ti[0] -= d-c;
        }
        for(ll i = 0; i<aj; ++i){
            cin >> c >> d;
            J[ac + i] = make_pair(make_pair(c, d), 1);
            ti[1] -= d-c;
        }
        sort(J.begin(), J.end());
        for(ll i = 0; i<n; ++i){
            if(J[i].first.second == J[(i+1)%n].first.first and J[i].second == J[(i+1)%n].second){
                J[i].first.second = J[(i+1)%n].first.second;
                J.erase(J.begin()+(i+1)%n);
                --i;
            }
        }
        ll res = 0, v = -1;
        while(true){
            m[0] = ti[0], m[1] = ti[1], j[0] = -1, j[1] = -1;
            for(ll i = 0; i<n; ++i){
                if(((J[(i+1)%n].first.first - J[i].first.second + 1440)%1440 <= m[J[i].second]) and J[i].second == J[(i+1)%n].second){
                    m[J[i].second] = (J[(i+1)%n].first.first - J[i].first.second + 1440)%1440;
                    j[J[i].second] = i;
                }
            }
            if(j[0] == -1 and ti[0]!=720){
                v = 0;
                break;
            }
            if(j[1] == -1 and ti[1]!=720){
                v = 1;
                break;
            }
            if(ti[0]!=720 and ti[1]!=720)
                if(j[1]>(j[0]+1)%n)
                    --j[1];
            if(ti[0]!=720){
                J[j[0]].first.second = J[(j[0]+1)%n].first.second;
                J.erase(J.begin()+(j[0]+1)%n);
                ti[0] -= m[0];
            }
            if(ti[1]!=720){
                J[j[1]].first.second = J[(j[1]+1)%n].first.second;
                J.erase(J.begin()+(j[1]+1)%n);
                ti[1] -= m[1];
            }
        }
        for(ll i = 0; i<n; ++i){
            if(J[i].second == v){
                res += 2;
            }
        }
        cout << "Case #" << t+1 << ": " << res << endl;
    }
    return 0;
}
