#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

bool Work(vector<int> &a, vector<int> &ans, int len) {
    if (len < 0) {
        return true;
    }
    ans[len] = a[len];
    if ((len + 1 == a.size() || ans[len] >= ans[len + 1]) && Work(a, ans, len - 1)) {
        return true;
    }
    ans[len]--;
    if (len + 1 < a.size() && ans[len] < ans[len + 1]) {
        return false;
    } else {
        for (int i = len - 1; i >= 0; i--) {
            ans[i] = 9;
        }
        return true;
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        long long num;
        scanf("%lld", &num);
        vector<int> a;
        while (num) {
            a.push_back(num % (long long)10);
            num /= (long long)10;
        }
        vector<int> ans(a.size(), 0);
        Work(a, ans, a.size() - 1);
        long long res = 0;
        for (int i = ans.size() - 1; i >= 0; i--) {
            res = res * (long long)10 + ans[i];
        }
        printf("Case #%d: %lld\n", t, res);
    }
    return 0;
}
