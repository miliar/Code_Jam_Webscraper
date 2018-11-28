#include <bits/stdc++.h>
#define FI(i, a, b) for (int i = (a); i <= (b); i++)
#define FD(i, a, b) for (int i = (a); i >= (b); i--)
using namespace std;
using LL = long long;

void work(int testCase) {
    LL number;
    scanf("%lld", &number);
    LL tmp = number;
    vector<int> digits;
    while (number) {
        digits.push_back(number % 10);
        number /= 10;
    }
    reverse(digits.begin(), digits.end());
    vector<int> ans = digits;
    for (int i=1;i<ans.size();i++) ans[i] = 9;
    for (int i=1;i<ans.size();i++) {
        if (digits[i] < digits[i-1]) {
            int j = i-1;
            while (j >= 0) {
                ans[j]--;
                if (j==0 || ans[j]>=ans[j-1]) break;
                ans[j] = 9;
                j--;
            }
            printf("Case #%d: ", testCase);
            for (int j=0;j<ans.size();j++) {
                if (j==0 && ans[j]==0) continue;
                printf("%d", ans[j]);
            }
            printf("\n");
            return;
        } else ans[i] = digits[i];
    }
    printf("Case #%d: %lld\n", testCase, tmp);
}
int main() {
    int T;
    scanf("%d", &T);
    FI(i, 1, T)
    work(i);
}