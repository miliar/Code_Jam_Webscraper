
#include <iostream>
#include <queue>
using namespace std;

typedef long long ll;

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    	freopen("ans.txt", "w", stdout);
    
    int t;
    cin >> t;
    ll n,k;
    for (int it = 1; it <= t; ++it) {
        cout<<"Case #"<<it<<": ";
        priority_queue<ll> q;
        cin >> n >> k;
        
        
        ll mmin, mmax;
        
        ll cur = n;
        for(ll j = 1; j <= k; j++) {
                if(!q.empty()) {
                    cur = q.top();
                    q.pop();
                }
                if(cur>0) {
                    if(cur&1) {
                        mmin = (cur-1)/2;
                        mmax = mmin;
                    }
                    else {
                        mmin = cur/2-1;
                        mmax = cur/2;
                    }
            }
            //cout << cur << ", ";
            q.push(mmax);
            q.push(mmin);
            
        }
        cout << mmax << " " << mmin << "\n";
    }

    return 0;
}
