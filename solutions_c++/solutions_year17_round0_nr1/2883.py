#include <bits/stdc++.h>
using namespace std;

inline void flip(char &x) {
    x = x == '+' ? '-' : '+';
}

int trial(string s, int k) {
    auto n = (int)s.length();
    int ans = 0;
    for(int i = 0 ; i < n ; i++) {
        if (s[i] == '-') {
//            cerr << i << endl;
            if (n-i < k) {
                return 1e6;
            }
//            cerr << "FLIPPING FROM: " << " " << i << endl;

            for(int j = 0 ; j < k ; j++) {
                flip(s[i+j]);
//                cerr << "Made flip" << " " << i+j << " " << s <<  endl;
            }
            ans++;
        }
    }
    return ans;
}

void solve() {
    string s; int k;
    cin >> s >> k;
    int ans = trial(s, k);
//    cerr << "TRIAL1 : " << " " << trial(s, k) << " " << ans <<endl;
    reverse(s.begin(), s.end());
    ans = min(trial(s, k), ans);
//    cerr << "TRIAL2 : " << " " << trial(s, k) << " " << ans << endl;
    if (ans > 5e4) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cout << ans << endl;
    }
    
}

int main(int argc, const char **argv) {
    if(argc>=2) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++) {
        printf("Case #%d: ", t);
        solve();
        fprintf(stderr, "Finished case %d\n\n", t);
    }
}
