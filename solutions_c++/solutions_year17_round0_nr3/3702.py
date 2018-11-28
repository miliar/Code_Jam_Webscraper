#include <bits/stdc++.h>
using namespace std;

int n, k, t;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;

    for(int caseno = 1; caseno <= t; caseno ++){
        cin >> n >> k;
        priority_queue<pair<int, int> > pq;
        pq.push({n, n});

        for(int i=1; i<k; i++) {
            pair<int, int> range = pq.top(); pq.pop();
            int x = n - range.second, d = range.first;
            pq.push({(d + 1) / 2 - 1, n - x});
            pq.push({d - (d + 1) / 2, n - (x + (d + 1) / 2)});
        }

        pair<int, int> range = pq.top(); pq.pop();
        int d = range.first;
        cout << "Case #" << caseno << ": "
            << max((d + 1) / 2 - 1, d - (d + 1) / 2) << ' '
            << min((d + 1) / 2 - 1, d - (d + 1) / 2) << '\n';
    }
}
