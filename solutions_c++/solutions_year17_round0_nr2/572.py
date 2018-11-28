#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

char s[10001];

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        long long n;
        scanf("%I64d", &n);
        long long x = n;
        vector<int> digits;
        while (x) {
            digits.push_back(x % 10);
            x /= 10;
        }
        reverse(digits.begin(), digits.end());

        bool valid = true;
        for (int i = 1; i < digits.size(); ++ i) {
            valid &= digits[i] >= digits[i - 1];
        }
        long long answer = 0;
        if (valid) {
            answer = n;
        } else {
            for (int i = 1; i < digits.size(); ++ i) {
                answer = answer * 10 + 9;
            }
            long long prefix = 0;
            for (int firstSmall = 0; firstSmall < digits.size(); ++ firstSmall) {
                int mini = (firstSmall == 0) ? 1 : digits[firstSmall - 1];
                if (mini < digits[firstSmall]) {
                    long long x = prefix * 10 + digits[firstSmall] - 1;
                    for (int i = firstSmall + 1; i < digits.size(); ++ i) {
                        x = x * 10 + 9;
                    }
                    answer = max(answer, x);
                }
                if (firstSmall > 0 && digits[firstSmall] < digits[firstSmall - 1]) {
                    break;
                }
                prefix = prefix * 10 + digits[firstSmall];
            }
        }
        printf("Case #%d: %I64d\n", test, answer);
    }
    return 0;
}
