#include <bits/stdc++.h>
using namespace std;

int test(string & s) {
    if (s[0] == s[s.length()-1]) {
        return 0;
    }
    for(int i = 1 ; i < s.length() ; i++) {
        if (s[i] == s[i-1]) {
            return 0;
        }
    }
    return 1;
}

int solve() {
    int n;
    cin >> n;
    int r, o, y, g, b, v;
    cin >> r >> o >> y >> g >> b >> v;
    
    string gs = "", os = "", vs = "";
    string np = "IMPOSSIBLE";
    int f = 0;
    while (g) {
        r--;
        g--;
        gs += "RG";
    }
    while (o) {
        b--;
        o--;
        os += "BO";
    }
    while (v) {
        y--;
        v--;
        vs += "YV";
    }
    
    if (gs.length() + os.length() + vs.length() == max({gs.length(), vs.length(), os.length(), (size_t)1}) ) {
        if (r < 0 || y < 0 || b < 0) {
            cout << np << endl;
            return 0;
        }
        if (r == 0 && b == 0 && g == 0) {
            cout << gs + vs + os << endl;
            return 0;
        }
    }
    
    int gf = 0, vf = 0, of = 0;
    if (gs.length() >= 1) {
        if (r) {
            gs += "R";
            gf = 1;
        }
        else {
            f = 1;
        }
    }
    
    if (vs.length() >= 1) {
        if (y) {
            vs += "Y";
            vf = 1;
        }
        else {
            f = 1;
        }
    }
    
    if (os.length() >= 1) {
        if (b) {
            os += "B";
            of = 1;
        }
        else {
            f = 1;
        }
    }
    
    if (f) {
        cout << np << endl;
//        cerr << r << " " << y << " " << b <<  endl;

        return 0;
    }
    int mx = max({r, y, b});
    
    pair<int, char> z[3];
    z[0] = {r, 'R'};
    z[1] = {y, 'Y'};
    z[2] = {b, 'B'};
    
    sort(z, z+3);
    reverse(z, z + 3);
    
    if (z[0].first > z[1].first + z[2].first) {
        cout << np << endl;
//        cerr << r << " " << y << " " << b <<  endl;
        return 0;
    }
    

    
//    cerr << "PAIR ARR" << endl;
//    for(auto u:z) {
//        cerr << u.first << " " << u.second << endl;
//
//    }
    
    int pp = z[1].first + z[2].first - z[0].first;
    
    string ans = "";
    
    for(int i = 0 ; i < z[0].first ; i++) {
        ans += z[0].second;
        if (z[1].first) {
            ans += z[1].second;
            if (pp > 0) {
                pp--;
                ans += z[2].second;
            }
            z[1].first--;
        }
        else {
            ans += z[2].second;
        }
    }
//    cerr << os << " " << gs << " " << vs << endl;
//    cerr << of << " " << gf << " " << vf << endl;
//    cerr << ans << endl;
    string ans2 ="";
    
    for(int i = 0 ; i < ans.length() ; i++) {
        if (gf && ans[i] == 'R') {
            ans2 += gs;
            gf = 0;
        }
        else if (vf && ans[i] == 'Y') {
            ans2 += vs;
            vf = 0;
        }
        else if (of && ans[i] == 'B') {
            ans2 += os;
            of = 0;
        }
        else {
            ans2 += ans[i];
        }
    }
    
    assert(test(ans2) && ans2.length() == n);
    cout << ans2 << endl;
    return 0;
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
