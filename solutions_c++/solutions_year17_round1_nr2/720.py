#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>

using namespace std;

#define ll long long
#define N (ll)(1e6+5)
#define INF (ll)(1e18+3)
#define EPS (1e-9)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    int t;
    in >> t;
    
    for (int i = 0; i < t; i++) {
        
        int n, p;
        in >> n >> p;
        int r[n];
        vector<vector<int>> q(n);
        vector<vector<pair<int, int>>> minmax(n);
        for (int j = 0; j < n; ++j)
            in >> r[j];
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < p; ++k) {
                int tmp;
                in >> tmp;
                q[j].push_back(tmp);
            }
            sort(q[j].begin(), q[j].end());
        }
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < p; ++k) {
                int tmp = q[j][k];
                double copy = (1.0 * tmp) / r[j];
                cout << "copy : " << copy << endl;
                int min = ceil(copy / 1.10);
                int max = floor(copy / 0.90);
                minmax[j].push_back({min, max});
            }
        }
        int ans = 0;
        vector<int> id(n, 0);
        bool done = false;
        for (int j = 0; j < p; ++j) {
            pair<int, int> tmp = minmax[0][j];
            for (int serving = tmp.first; serving <= tmp.second; serving++) {
                bool success = true;
                int init[n];
                for (int k = 0; k < n; k++) {
                    init[k] = id[k];
                    while (serving > minmax[k][init[k]].second && init[k] < p) init[k]++;
                    if (init[k] == p || serving < minmax[k][init[k]].first) {
                        success = false;
                        break;
                    }
                }
                if (success) {
                    ans++;
                    for (int k = 0; k < n; k++) {
                        id[k] = init[k] + 1;
                        if (id[k] == p) {
                            done = true;
                            break;
                        }
                    }
                    break;
                }
                
            }
            if (done) break;
        }
        
        out << "Case #" << i + 1 << ": " << ans << endl;
    }
    
    in.close();
    out.close();
}
