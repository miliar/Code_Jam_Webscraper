#include <iostream>
#include <map>
#include <queue>

using namespace std;
typedef long long ll;

void solve()
{
    ll N,K;
    cin >> N >> K;

    priority_queue<ll> pq;
    map<ll, ll> cnt;

    cnt[N] = 1;
    pq.push(N);

    while(1) {
        ll large = pq.top();
        pq.pop();
        ll rooms = cnt[large];       
        ll big = large / 2;
        ll small = (large - 1) / 2;
        if (rooms >= K) {
            cout <<  big << " " << small << endl;
            return;
        }
        K -= rooms;

        if (cnt[big] == 0) pq.push(big);
        cnt[big] += rooms;
        if (cnt[small] == 0) pq.push(small);
        cnt[small] += rooms;
    }
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}