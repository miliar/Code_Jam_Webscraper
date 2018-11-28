#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

vector<int> pac;

void otoc(int od, int k) {
    for (int i = od; i<od+k; i++) {
        pac[i] = 1-pac[i];
    }
}

pair<int, int> plusminus(int od, int k) {
    int plus = 0, minus = 0;
    for (int i = od; i<od+k; i++) {
        if (pac[i] == 0) {
            minus++;
        } else {
            plus++;
        }
    }
    return {plus, minus};
}

int dasa(int od, int k) {
    if (od+k == pac.size()) {
        pair<int, int> plmi = plusminus(od, k);
        if (plmi.first == k) {
            return 0;
        }
        if (plmi.second == k) {
            return 1;
        }
        return 10047;
    }
    if (pac[od] == 1) {
        return dasa(od+1, k);
    }
    otoc(od, k);
    return 1+dasa(od+1, k);
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t<=T; ++t) {
        string s;
        int k;
        cin >> s >> k;
        pac.clear();
        for (unsigned i = 0; i<s.size(); ++i) {
            if (s[i] == '-') pac.push_back(0);
            else pac.push_back(1);
        }
        cout<<"Case #"<<t<<": ";
        int res = dasa(0, k);
        if (res >= 10047) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout<<res<<endl;
        }
    }
    return 0;
}
