//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

int n, c, m;
multiset<int> pos[3];

int main() {
    srand(31415); ios::sync_with_stdio(0);
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n >> c >> m;
        pos[1].clear();
        pos[2].clear();
        for (int i = 0; i < m; ++i) {
            int p, id;
            cin >> p >> id;
            pos[id].insert(p);
        }
        
        cout << "Case #" << t << ": ";
        
        int ans = 0, rr = 0;
        
        for (int rd = 0; ; ++rd) {
            if (pos[1].size() == 0 && pos[2].size() == 0) break;
            
            if (pos[1].size() == 0 || pos[2].size() == 0) {
                ans += pos[1].size() + pos[2].size();
                break;
            }
            
            ans++;
            
            int best1 = -1, cc1 = 0, best2 = -1, cc2 = -1;
            for (int i = 1; i <= n; ++i) {
                if (min(pos[1].count(i), pos[2].count(i)) > cc1) {
                    cc2 = cc1;
                    best2 = best1;
                    
                    cc1 = min(pos[1].count(i), pos[2].count(i));
                    best1 = i;
                } else if (min(pos[1].count(i), pos[2].count(i)) > cc2) {
                    cc2 = min(pos[1].count(i), pos[2].count(i));
                    best2 = i;
                }
            }
            
            if (best1 == -1) {
                pos[1].erase(pos[1].begin());
                pos[2].erase(pos[2].begin());
                continue;
            }
            
            if (cc1 != pos[1].count(best1)) {
                swap(pos[1], pos[2]);
            }
            
            if (pos[1].count(best1) == pos[1].size()) {
                if (best1 == 1) {
                    pos[2].erase(pos[2].find(best1));
                } else {
                	pos[1].erase(pos[1].find(best1));
                    pos[2].erase(pos[2].find(best1));
                    rr++;
                }
                continue;
            }
            pos[2].erase(pos[2].find(best1));
            if (best2 != -1) {
                pos[1].erase(pos[1].find(best2));
            } else {
            	auto it = pos[1].begin();
            	while (*it == best1) it++;
                pos[1].erase(it);
            }
        }
        cout << ans << " " << rr << "\n";
    }
    return 0;
}
