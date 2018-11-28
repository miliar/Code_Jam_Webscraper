#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


vector<int> toDigitsVector(long long n) {
    vector<int> result;
    while (n > 0) {
        result.push_back(n % 10);
        n /= 10;
    }
    return result;
}


long long toNumber(vector<int> digits) {
    long long result = 0;
    reverse(digits.begin(), digits.end());
    for (int digit : digits) {
        result = result * 10 + digit;
    }
    return result;
}


long long findMaxTidyNumber(long long n) {
    vector<int> digits = toDigitsVector(n);
    int pLen = 1;
    int numDigits = digits.size();
    while (pLen < numDigits && digits[numDigits - pLen] <= digits[numDigits - pLen - 1]) {
        ++pLen;
    }
    if (pLen == numDigits) {
        return n;
    }
    while (pLen > 1 && digits[numDigits - pLen] == digits[numDigits - pLen + 1]) {
        --pLen;
    }
    --digits[numDigits - pLen];
    while (pLen < numDigits) {
        ++pLen;
        digits[numDigits - pLen] = 9;
    }
    while (digits.back() == 0) {
        digits.pop_back();
    }
    return toNumber(digits);
}


int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    for (int testId = 0; testId < numTests; ++testId) {
        long long n;
        cin >> n;
        cout << "Case #" << testId + 1 << ": " << findMaxTidyNumber(n) << endl;
    }
    return 0;
}
