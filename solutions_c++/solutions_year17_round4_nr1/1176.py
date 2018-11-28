#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int N, P;
    cin >> N >> P;

    int ans = 0;
    if (P == 2) {
        bool odds = true;
        for (int i = 0; i < N; i++) {
            int x; cin >> x;
            if (x & 1) {
                if (odds) {
                    ans++;
                    odds = false;
                }
                else odds = true;
            }
            else ans++;
        }    
    }
    else if (P == 3) {
        vector<int> cnts(3);
        for (int i = 0; i < N; i++) {
            int x; cin >> x;
            cnts[x%3]++; 
        }
        
        int minc = min(cnts[1], cnts[2]);
        int maxc = max(cnts[1], cnts[2]);
        ans = cnts[0] + minc + (maxc-minc+2) / 3;
    }    

    else if (P == 4) {
        vector<int> cnts(4);
        for (int i = 0; i < N; i++) {
            int x; cin >> x;
            cnts[x%4]++;
        }
        int minc = min(cnts[1], cnts[3]);
        int maxc = max(cnts[1], cnts[3]);
        bool r = (maxc - minc) & 1;
        int twos = (maxc - minc)/2 + cnts[2];
        r = r || twos & 1;
        ans = cnts[0] + minc + twos/2 + r;
    }

    cout << ans << endl;
}

int main (void) {
    int T; cin >> T;

    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}
