#include<iostream>
#include<cmath>
#include<cstdio>
#include<map>
#include<algorithm>

typedef long long ll;

using namespace std;

int K;
int l;

void flip(string & s, int i, ll & score ) {
    for (int j=i;j<i+K;++j) {
        if (s[j] == '-') {
            s[j] = '+';
            ++score;
        } else {
            s[j] = '-';
            --score;
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int c=1;c<=T;++c) {
        string s;
        cin >> s >> K;
        l = s.size();
        ll score = 0;
        for (int i=0; i<l; ++i) {
            if (s[i] == '+') ++score;
        }
        ll result = 0;
        for (int i=0; i<=l-K; ++i) {
            if (s[i] == '-') {
                flip(s, i, score);
                ++result;
            }
        }
        if (score == l)
            cout << "Case #" << c << ": " << result << endl;
        else
            cout << "Case #" << c << ": IMPOSSIBLE" << endl;
    }
}

