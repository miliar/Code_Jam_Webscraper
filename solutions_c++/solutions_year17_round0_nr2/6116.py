#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
int tests;
long long N;

vector<int> toDigits(long long N) {
    assert(N > 0);
    vector<int> result;
    while (N) {
        result.push_back(N % 10);
        N /= 10;
    }

    reverse(result.begin(), result.end());
    return result;
}

bool canSetDigit(vector<int>& digits, int digitIdx, int chosenDigit) {
    while (digitIdx + 1 < digits.size() && digits[digitIdx + 1] == chosenDigit) {
        digitIdx++;
    }

    return digitIdx + 1 == digits.size() || digits[digitIdx + 1] > chosenDigit;
}

long long get(vector<int>& digits, int digitIdx, long long soFar) {
    if (digits.size() == digitIdx) {
        return soFar;
    }

    int currDigit = digits[digitIdx];
    if (canSetDigit(digits, digitIdx, currDigit)) {
        return get(digits, digitIdx + 1, soFar * 10 + currDigit);
    }

    // set currDigit - 1 + 999
    soFar = soFar * 10 + (currDigit - 1);
    for (size_t i = digitIdx + 1; i < digits.size(); i++) {
        soFar = soFar * 10 + 9;
    }

    return soFar;
}

int main() {
    freopen("tidyNumbers.in", "r", stdin);
    freopen("tidyNumbers.out", "w", stdout);

    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        scanf("%lld", &N);

        vector<int> digits = toDigits(N);

        printf("Case #%d: %lld\n", test, get(digits, 0, 0));
    }
    return 0;
}