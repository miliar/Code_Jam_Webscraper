#include "bits/stdc++.h"
#include <cassert>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define ll64 long long

const int MAXN = 1005;

int n[30];
int a[30];

bool is_tidy(long long num) {
    int last = 9;
    while (num > 0) {
        int d = num % 10;
        num /= 10;
        if (d > last) {
            return false;
        }
        last = d;
    }
    return true;
}

long long stupid_solve(long long num) {
    for (int i = num; i > 0; i--) {
        if (is_tidy(i)) {
            return i;
        }
    }
    assert(false);
}

long long solve(long long num) {
    long long orig_num = num;
    int l = 0;
    while (num > 0) {
        n[l] = num % 10;
        num /= 10;
        l++;
    }
    for (int i = 0; i < l / 2; i++) {
        swap(n[i], n[l - 1 - i]);
    }
    for (int i = 0; i < l; i++) {
        bool ok = true;
        for (int k = i; k < l; k++) {
            if (n[i] < n[k]) {
                break;
            }
            ok &= n[i] <= n[k];
        }
        if (ok) {
            a[i] = n[i];
            continue;
        }

        assert(n[i] > 0);
        a[i] = n[i] - 1;
        for (int j = i + 1; j < l; j++) {
            a[j] = 9;
        }
        break;
    }
    long long answer = 0;
    for (int i = 0; i < l; i++) {
        answer = answer * 10 + a[i];
        assert(i == 0 || a[i - 1] <= a[i]);
    }
    assert(answer <= orig_num);

    /*
    int true_ans = stupid_solve(orig_num);
    if (true_ans != answer) {
        cerr << "fail: " << true_ans << " " << answer << " " << orig_num << endl;
        assert(false);
    }
    */
    return answer;
}

int main() {
    #ifdef LOCAL_RUN
        freopen("Blg", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int t;
    cin >> t;

    long long n;
    for (int i = 0; i < t; i++) {
        cin >> n;
        cout << "Case #" << (i + 1) << ": " << solve(n) << endl;
    }

    return 0;
}
