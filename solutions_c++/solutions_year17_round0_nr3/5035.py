#include <bits/stdc++.h>

#define TASK "C-small-2-attempt0"

using namespace std;

map<long long, long long> len;

void solve(int num){
    cout << "Case #" << num << ": ";
    len.clear();
    long long n, k;
    cin >> n >> k;
    len[n] = 1;
    pair<long long, long long> cur;
    while (true){
        cur = *len.rbegin();
        if (cur.second >= k){
            cout << ceil((double)(cur.first - 1) / 2) << ' ' << (cur.first - 1) / 2 << '\n';
            return;
        }
        k -= cur.second;
        len[(cur.first - 1) / 2] += cur.second;
        len[ceil((double)(cur.first - 1) / 2)] += cur.second;
        len.erase(cur.first); 
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) solve(i);
    return 0;
}
