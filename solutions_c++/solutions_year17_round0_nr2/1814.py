#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

lld solve(lld n) {
    lld saven = n;
    vector<int> digits;
    while (n) {
        digits.push_back(n % 10);
        n /= 10;
    }
    reverse(digits.begin(), digits.end());
    for (int i = 0; i < digits.size() - 1; i++) {
        if (digits[i + 1] >= digits[i]) {
            continue;
        }
        // Find first one that can be downgraded
        for (int j = i; j >= 0; j--) {
            if ((j > 0 && digits[j] - 1 >= digits[j - 1])
                || (j == 0 && digits[j] > 1)) {
                digits[j]--;
                for (int p = j + 1; p < digits.size(); p++) {
                    digits[p] = 9;
                }
                lld ret = 0;
                for (int p = 0; p < digits.size(); p++) {
                    ret = ret * 10 + digits[p];
                }
                return ret;
            }
        }
        // Return all 9s
        lld ret = 0;
        for (int j = 0; j < digits.size() - 1; j++) {
            ret = ret * 10 + 9;
        }
        return ret;
    }
    return saven;
}

int main() {
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        lld n;
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", t, solve(n));
    }
    return 0;
}
