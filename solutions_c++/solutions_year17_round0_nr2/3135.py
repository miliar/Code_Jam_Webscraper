#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;
typedef long double ld;
const double PI = acos(-1.);

void getTest(ll &N) {
    //N = rand() % 10000 + 1;
    cin >> N;
    return;
}

int getNumDig(ll N) {
    vector<int> digits;
    while (N) {
        digits.push_back(N % 10);
        N /= 10;
    }
    return digits.size();
}

bool check(ll N) {
    vector<int> digits;
    while (N) {
        digits.push_back(N % 10);
        N /= 10;
    }
    for (int i = digits.size() - 2; i > -1; --i) {
         if (digits[i] < digits[i + 1]) {
             return false;
         }
    }
    return true;
}

ll brute(ll N) {
    ll res = 1;
    for (int i = 2; i <= N; ++i) {
        if (check(i)) {
            res = i;
        }
    }
    return res;
}

ll getNum(vector<int> &digits) {
    ll res = 0;
    for (int digit : digits) {
        res = res * 10 + digit;
    }
    return res;
}

ll solve(ll N) {
    int nlen = getNumDig(N);
    ll res = 0;
    vector<int> pref(nlen, 0);
    for (int i = 0; i < nlen; ++i) {
        for (int digit = 0; digit < 10; ++digit) {
            vector<int> cand(pref);
            cand[i] = digit;
            int next = digit;
            if (digit == 0) next = 9;
            for (int j = i + 1; j < nlen; ++j) {
                cand[j] = next;
            }
            ll cur = getNum(cand);
            if (cur > res && check(cur) && cur <= N) {
                res = cur;
                pref = cand;
            }
        }
    }

    return res;
}

int main() {

    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    srand(time(nullptr));
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll N;
        getTest(N);
        cout << "case #" << t << ": " << solve(N) << endl;
//        if (solve(N) != brute(N)) {
//            cout << "WA\n";
//            cout << N << endl;
//            cout << brute(N) << " " << solve(N) << endl;
//            return 0;
//        }
//        cout << "OK " << t << endl;
    }
    return 0;
}