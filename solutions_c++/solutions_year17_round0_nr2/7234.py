#include <bits/stdc++.h>
using namespace std;

int T;
string s, t;
int n;

void prop(int idx) {
    if(idx==0) return;
    if(t[idx]-'0' < t[idx-1]-'0') {
        t[idx-1] = (int)t[idx-1]-1;
        t[idx] = '9';
        prop(idx-1);
    }
}

void solve() {
    for(int i=0;i<n-1;i++) {
        if(s[i]-'0' <= s[i+1]-'0') {
            t[i] = s[i];
        } else {
            t[i] = (int)s[i] - 1;
            for(int j=i+1;j<n;j++) t[j] = '9';
            prop(i);
            return;
        }
    }
}

void print() {
    bool start=true;
    for(int i=0;i<t.size();i++) {
        if(start && t[i] == '0') continue;
        start = false;
        cout << t[i];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin >> T;
    for(int i=1;i<=T;i++) {
        cin >> s;
        n = s.size();
        t.clear();
        for(int _=0;_<n;_++) {
            t += '-';
        }
        t[n-1] = s[n-1];
        solve();
        cout << "Case #" << i << ": ";
        print();
        cout << endl;
    }
}
