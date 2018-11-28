#include<bits/stdc++.h>
using namespace std;

bool is_tidy(unsigned long long candidate) {
    unsigned long long last = candidate%10ULL;
    while(candidate>0ULL) {
        unsigned long long current = candidate%10ULL;
        candidate /= 10ULL;
        if(current>last) return false;
        last = current;
    }
    return true;
}


static const int dbg = 0;
#define dout if(dbg)cout

void solve() {
    unsigned long long T;
    cin >> T;
    if(is_tidy(T)) {
        cout << T << endl;
        return;
    }
    string s = to_string(T);
    int ones_ended = -1;
    int flipping_point = -1;
    for(int i=0; i<s.length(); ++i) {
        if(ones_ended == i-1 && s[i] == '1') {
            ones_ended = i;
        }
        if(i>0 && flipping_point < 0 && s[i]<s[i-1]) {
            flipping_point = i-1;
        }
    }
    if(flipping_point == ones_ended) {
        for(int i=0; i<s.length()-1; ++i) cout << "9";
        //for(int i=0; i<s.length()-ones_ended-1; ++i) cout << "9";
        cout << endl;
        return;
    }
    for(int i=0; i<flipping_point; ++i) {
        cout << s[i];
    }
    cout << (s[flipping_point] - '0' -1);
    for(int i=flipping_point + 1; i<s.length(); ++i) {
        cout << '9';
    }
    cout << endl;
    return;
}

int main() {
    int n_testcases, start_number;
    scanf("%d", &n_testcases);
    for(int i=1; i<=n_testcases; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
