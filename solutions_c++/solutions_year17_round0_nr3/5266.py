#include <bits/stdc++.h>
#define optimezeio ios_base::sync_with_stdio(0);cin.tie
#define lli long long int

using namespace std;

int main () {
    optimezeio(0);
    int t = 0;

    cin >> t;

    for (int l = 1; l <= t; ++l)
    {
        lli n = 0, k = 0;
        priority_queue<int> pq;
        cin >> n >> k;
        lli cuantos = 1;
        pq.push(n);
        while(!pq.empty()) {
            lli tmp = pq.top();
            pq.pop();

            if (cuantos == k) {
                if (tmp % 2 != 0) {
                    lli val = (tmp - 1) / 2;
                    cout << "Case #" << l << ": " << val << " " << val << endl;
                } else {
                    lli val = tmp / 2;
                    cout << "Case #" << l << ": " << val << " " << val - 1 << endl;
                }
                
                
                break;
            }

            if (tmp % 2 != 0) {
                lli val = (tmp - 1) / 2;
                pq.push(val);
                pq.push(val);
            } else {
                lli val = tmp / 2;
                pq.push(val);
                pq.push(val - 1);
            }
            cuantos++;
        }
    }

    return 0;
}