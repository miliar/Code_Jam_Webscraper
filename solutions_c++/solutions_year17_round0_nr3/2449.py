#include <bits/stdc++.h>
using namespace std;

typedef long long llong;

void solve(llong n, llong k){
    set<llong> q;
    unordered_map<llong, llong> count;
    count[n] = 1;
    q.insert(-n);
    while (k){
        llong v = -*q.begin();
        q.erase(q.begin());
        llong a = v/2, b = (v-1)/2;

        if (k <= count[v]){
            cout << a << " " << b << endl;
            return;
        }

        k -= count[v];

        if (count.find(a) == count.end())
            count[a] = 0;
        if (count.find(b) == count.end())
            count[b] = 0;
        count[a] += count[v]; count[b] += count[v];
        q.insert(-a); q.insert(-b);
    }
}

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        llong n, k;
        cin >> n >> k;
        cout << "Case #" << cases++ << ": ";
        solve(n, k);

    }
    return 0;
}
