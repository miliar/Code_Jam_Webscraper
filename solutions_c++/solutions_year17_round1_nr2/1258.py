#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define print(x) cout << x << endl
#define input(x) cin >> x

typedef long long llint;

class Solution {
public:
    Solution(
            int n_, 
            int p_, 
            map<int, vector<int> >& mp1, 
            map<int, vector<int> >& mp2) {
        n = n_;
        p = p_;
        tot = n * p;
        g.clear();
        g.resize(tot);

        for (auto p: mp1) {
            int key = p.first;
            const vector<int>& v = p.second;

            for (auto peer: mp2[key]) {
                for (auto node: v) {
                    g[node].push_back(peer);
                }
            }
        }
    }

    bool deal(int x) {
        for (auto i: g[x]) {
            if(!visit[i]) {
                visit[i]=true;
                if(pre[i]==-1 || deal(pre[i])) {
                    pre[i]=x;
                    return true;
                }
            }
        }
        return false;
    }

    int solve() {
        int sum = 0;
        pre = vector<int>(tot, -1);
        for(int i=0;i<n;i++)
        {
            visit = vector<bool>(tot, false);
            if(deal(i)) sum++;
        }
        return sum;
    }
private:
    int tot, n, p;
    vector<vector<int> > g;
    vector<int> pre;
    vector<bool> visit;
};


int main() {
    // freopen("b.txt", "r", stdin);
    int T;
    input(T);
    for (int case_ = 0; case_ < T; case_++) {
        printf("Case #%d: ", case_ + 1);

        int n, p;
        input(n >> p);

        vector<int> units(n);
        for (int i = 0; i < n; i++) {
            input(units[i]);
        }

        map<int, vector<int> > packets[2];
        int tot = 0;

        for (int i = 0; i < n; i++) {
            int u;
            for (int j = 0; j < p; j++) {
                input(u);
                int a = u / 1.1 / units[i];
                int b = u / 0.9 / units[i];
                
                bool flag = false;
                for (llint k = a; k <= b; k++) {
                    if (k * units[i] * 0.9 <= u && k * units[i] * 1.1 >= u) {
                        if (packets[i].count(k) == 0) {
                            packets[i][k] = vector<int>();
                        }
                        packets[i][k].push_back(i * p + j);
                        flag = true;
                    }
                }
                if (flag) {
                    tot++;
                }
            }
        }
        if (n == 1) {
            print(tot);
        } else {
            Solution S(n, p, packets[0], packets[1]);
            print(S.solve());
        }
    }
    return 0;
}
