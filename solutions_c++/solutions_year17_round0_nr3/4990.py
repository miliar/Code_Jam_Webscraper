#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define PI acos(-1)
#define endl '\n'
using namespace std;

typedef long long ll;
typedef pair<ll, ll> limit;
typedef pair<ll, limit> sector;

sector simulate(ll n, ll k) {

    priority_queue<sector> pq;
    vector<ll> sequence;

    pq.push(mp(n, mp(0, n + 1)));
    ll occupied = 0;

    sector result;

    while(sequence.size() < k) {

        sector next = pq.top();
        pq.pop();

        ll newPosition = next.se.fi + next.fi / 2;
        if(next.fi % 2 != 0)
            newPosition++;

        result = mp(newPosition, mp(next.se.fi, next.se.se));
        //cout << "(" << next.se.fi << "," << next.se.se << ") = " << newPosition << endl;

        sequence.pb(newPosition);
        pq.push(mp(newPosition - next.se.fi - 1, mp(next.se.fi, newPosition)));
        pq.push(mp(next.se.se - newPosition - 1, mp(newPosition, next.se.se)));

    }    
    return result;
}

int main() {

    int t;
    ll n, k;
    cin >> t;

    for(int i = 1; i <= t; i++) {

        cin >> n >> k;
        sector s = simulate(n, k);
        cout << "Case #" << i << ": " << max(s.fi - s.se.fi, s.se.se - s.fi) - 1 << " " << min(s.fi - s.se.fi, s.se.se - s.fi) - 1 << endl;

    }

    return 0;
}
