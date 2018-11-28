#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<int> toDigits(ll num) {
    vector<int> ret;
    while(num) {
        ret.push_back(num%10);
        num /= 10;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

ll append(ll a, ll b) {
    ll tmp = b;
    while(tmp) {
        tmp /= 10;
        a *= 10;
    }
    return a + b;
}

ll dp(int ind, int minCanUse, int isLimited, ll mem[30][100][2], const vector<int>& digits) {
    if(ind >= digits.size()) {
        return 0;
    }
    ll &ref = mem[ind][minCanUse][isLimited];
    if(ref != -1ll) {
        return ref;
    }
    ref = 0;
    
    if(isLimited) {
        for(int i = minCanUse; i<= digits[ind]; i++) {
            ref = max(ref, append(i, dp(ind + 1, i, i == digits[ind], mem, digits)));
        }
    } else {
        ref = append(9, dp(ind + 1, 9, 0, mem, digits));
    }

    return ref;
}

ll solve() {
    ll mem[30][100][2] = {};
    memset(mem, -1ll, sizeof mem);
    // cout << " # " << dp(0, 0, 1, mem, {1})<<endl;
    // exit(0);
    ll num;
    cin >> num;
    auto digits = toDigits(num);

    // cout << "# : " << num << " = ";
    // for(auto digit: digits) {
    //     cout << digit << " ";
    // }
    // cout << endl;

    return dp(0, 0, 1, mem, digits);
}

int main() {
    
    int tests;
    cin >> tests;
    for(int i = 1 ;i <= tests; i++) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
