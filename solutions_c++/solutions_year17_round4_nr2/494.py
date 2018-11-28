#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    int tc; cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n, c, m, maxd = 0;
        cin >> n >> c >> m;
        vector <int> ticket;
        map<int, int> d;
        for (int i = 0; i < m; i++) {
            int p, b;
            cin >> p >> b;
            --b, --p;
            d[b] ++;
            maxd = max(maxd, d[b]);
            ticket.push_back(p);
        }
        sort(ticket.begin(), ticket.end());
        reverse(ticket.begin(), ticket.end());
        map<int, int> prom;
        int L = maxd - 1, R = m;
        while (R - L > 1) {
            int k = (R + L) / 2;
            bool ok = 1;
            vector <int> unmatch;
            map<int, int> d;
            for (int i = 0; i < ticket.size(); i ++) {
                if (d[ticket[i]] < k)
                    d[ticket[i]] ++;
                else
                    unmatch.push_back(ticket[i]);
            }
            int ind = n - 1;
            for (int i = 0; i < unmatch.size(); i ++) {
                ind = min(ind, unmatch[i]);
                while (ind >= 0 && d[ind] == k)
                    ind--;
                if (ind < 0) {
                    ok = 0;
                    break;
                }
                d[ind] ++;
            }
            if (ok) {
                R = k;
                prom[k] = unmatch.size();
            }
            else
                L = k;
        }
        cout << "Case #" << t << ": ";
        cout << R << " " << prom[R] << endl;
    }
    return 0;
}
