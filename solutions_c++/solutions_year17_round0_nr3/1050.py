#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    int T, t;
    ll N, K;
    cin >> T;
    for (t = 1; t <= T; t++) {
        cin >> N >> K;
        unordered_map<ll,ll> m;
        priority_queue<ll, vector<ll>, less<ll> > q;
        
        q.push(N-1); m[N-1]++;
        while (K > 1) {
            ll t = q.top(); q.pop();
            ll ad = m[t];
            K -= ad;
            if (K < 1) q.push(t);
            ll ins = t/2;

            ll n1 = ins-1, n2 = t-(ins+1);
            if (m[n1] == 0) q.push(n1); m[n1] += ad;
            if (m[n2] == 0) q.push(n2); m[n2] += ad;
        }

        ll diff = q.top();
        cout << "Case #" << t << ": " << (diff+1)/2 << ' ' << diff/2 << endl;
    }
}