#include <bits/stdc++.h>
 
using namespace std;

int N, M, C;
vector<vector<int>> cnt;
 
void solve() {
    cin >> N >> C >> M;
    cnt.clear();
    cnt.assign(C, vector<int>(N));
    vector<int> pc(C);
    for (int i = 0; i < M; ++i) {
        int P, B;
        cin >> P >> B;
        P--;
        B--;
        cnt[B][P]++;
        pc[B]++;
    }
    int ansR = *max_element(pc.begin(), pc.end());
    int ansP = 0;
    while (true) {
        int sum = 0;
        ansP = 0;
        bool ok = true;
        for (int i = 0; i < N; ++i) {
            int sumHere = 0;
            for (int j = 0; j < C; ++j) {
                sumHere += cnt[j][i];
            }
            sum += sumHere;
            ansP += max(0, sumHere - ansR);
            if (sum > (i + 1) * ansR) {
                ok = false;
                break;
            }
        }
        if (ok) break;
        ++ansR;
    } 
    cout << ansR << " " << ansP;
}

int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
