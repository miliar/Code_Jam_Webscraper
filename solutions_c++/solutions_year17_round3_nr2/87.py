#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
using namespace std;

struct Slot {
    int f, t, i;
    bool operator<(const Slot &s) const {
        return f < s.f;
    }
};


typedef pair<int, int> pr;
int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ": ";
        vector<Slot> v;
        int n, m;
        cin >> n >> m;

        int consume[2] = {0, 0};
        for (int i = 0; i < n; ++i) {
            Slot s;
            cin >> s.f >> s.t;
            s.i = 0;
            v.push_back(s);
            consume[0] += s.t - s.f;
        }
        for (int i = 0; i < m; ++i) {
            Slot s;
            cin >> s.f >> s.t;
            s.i = 1;
            v.push_back(s);
            consume[1] += s.t - s.f;
        }
        sort(v.begin(), v.end());

        
        while (true) {
            pr merge[2];
            merge[0] = pr(9999999, -1);
            merge[1] = pr(9999999, -1);
            
            for (int i = 0; i < v.size(); ++i) {
                Slot a = v[i];
                Slot b = v[(i + 1) % v.size()];
                if (a.i != b.i) continue;
                if (b.f < a.f) {
                    b.f += 1440;
                }
                pr cur(b.f - a.t, i);
                if (cur < merge[a.i]) {
                    merge[a.i] = cur;
                }
            }
            if (consume[0] + merge[0].first <= 720) {
                int i = merge[0].second;
                consume[0] += merge[0].first;
                int nextI = (i + 1) % v.size();
                v[i].t = v[nextI].t;
                if (v[i].t < v[i].f) {
                    v[i].t += 1440;
                }
                v.erase(v.begin() + nextI);
            } else if (consume[1] + merge[1].first <= 720) {
                int i = merge[1].second;
                consume[1] += merge[1].first;
                int nextI = (i + 1) % v.size();
                v[i].t = v[nextI].t;
                if (v[i].t < v[i].f) {
                    v[i].t += 1440;
                }
                v.erase(v.begin() + nextI);
            } else {
                break;
            }
        }

        int exchange = 0;
        for (int i = 0; i < v.size(); ++i) {
            Slot a = v[i];
            Slot b = v[(i + 1) % v.size()];
            if (a.i != b.i) {
                ++exchange;
            } else {
                exchange += 2;
            }
        }
        exchange = max(2, exchange);
        cout << exchange << endl;
    }
}
