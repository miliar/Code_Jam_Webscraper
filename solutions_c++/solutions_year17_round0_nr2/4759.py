//Pranet Verma
#include <bits/stdc++.h>
using namespace std;
int f[1001];
bool isTidy(int u) {
    vector<int> digs;
    while (u > 0) {
        digs.push_back(u % 10);
        u /= 10;
    }
    reverse(digs.begin(), digs.end());
    vector<int> ndigs = digs;
    sort(ndigs.begin(), ndigs.end());
    return digs == ndigs;
}
int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    int t, tt = 0;
    cin >> t;
    for (int i = 1; i <= 1000; ++i) {
        f[i] = f[i - 1];
        if (isTidy(i)) {
            f[i] = i;
        }
    }
    while (t--) {
        cout << "Case #"<< ++tt << ": ";
        int n;
        cin >> n;
        cout << f[n] << endl;
    } 
}