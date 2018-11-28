#include <bits/stdc++.h>
 
using namespace std;

int N, P;
 
int solve() {
    cin >> N >> P;
    vector<int> count(P);
    for (int i = 0; i < N; ++i) {
        int g;
        cin >> g;
        count[g % P]++;
    }
    int ans = count[0] + 1;
    if (P == 4) {
        {
            int add = min(count[1], count[3]);
            ans += add;
            count[1] -= add;
            count[3] -= add;
        }
        {
            int add = count[2] / 2;
            ans += add;
            count[2] -= add * 2;
        }
        {
            int add = min(count[3] / 2, count[2]);
            ans += add;
            count[2] -= add;
            count[3] -= add * 2;
        }
        {
            int add = min(count[1] / 2, count[2]);
            ans += add;
            count[2] -= add;
            count[1] -= add * 2;
        }
    } else {
        for (int i = P - 1; i > 1; --i) {
            int add = min(count[1] / (P - i), count[i]);
            ans += add;
            count[1] -= add * (P - i);
            count[i] -= add;
        }
    }
    for (int i = 1; i < P; ++i) {
        ans += count[i] / P;
        count[i] -= count[i] / P * P;
    }
    int left = 0;
    for (int i = 1; i < P; ++i) {
        left += count[i];
    }
    if (left == 0) {
        ans--;
    }
    return ans;
}

int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        cout << solve();
        cout << endl;
    }
}
