#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())
#define LE(x) ((int)(x).length())


void solve() {
    int N, K; cin >> N >> K;
    vector<int> sizes = vector<int>(N + 1, 0);
    sizes[N] = 1;
    int biggest = N;
    int ans_s;
    int ans_l;
    while (K--){
        while (sizes[biggest] == 0) {
            biggest--;
        }
        int curr = biggest;
        sizes[biggest]--;
        if (curr % 2 == 1){
            ans_s = curr / 2;
            ans_l = curr / 2;
        } else {
            ans_s = curr / 2 - 1;
            ans_l = curr / 2;
        }
        sizes[ans_l]++;
        sizes[ans_s]++;
    }
    cout << ans_l << " " << ans_s << endl;
    
}
    

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++){
        cout << "Case #" << i+1 <<": ";
        solve();
    }
}
