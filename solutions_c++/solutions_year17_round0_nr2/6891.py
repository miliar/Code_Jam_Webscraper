#include <iostream>

typedef unsigned long long ULL;

using namespace std;

ULL exp10[19];

void preprocessExp10() {
    ULL p = 1;
    for (int i = 0; i < 19; i++) {
        exp10[i] = p;
        p *= 10;
    }
}

int getDigit(ULL n, ULL k) {
    return (n / exp10[k]) % 10;
}

ULL fixAtPoint(ULL n, ULL k) {
    ULL largePart = ((n / exp10[k]) - 1) * exp10[k];
    ULL smallPart = exp10[k] - 1;

    return largePart + smallPart;
}

int getLength(ULL n) {
    int length = 0;

    while (n > 0) {
        n /= 10;
        length ++;
    }

    return length;
}

bool isOK(ULL n, int k) {
    if (k == 0)
        return true;

    return getDigit(n, k) <= getDigit(n, k - 1);
}

int findFirstErrorFromLeft(ULL n) {
    for (int i = getLength(n) - 1; i > 0; i--) {
        if (!isOK(n, i))
            return i;
    }

    return 0;
}

ULL solve(ULL n) {
    int length = getLength(n);

    int firstError = findFirstErrorFromLeft(n);
    if (firstError == 0)
        return n;

    for (int i = firstError; i < length; i++) {
        if (!isOK(n, i))
            n = fixAtPoint(n, i);
    }

    return n;
}

int main() {
    preprocessExp10();

    int TN = 0;
    cin >> TN;

    for (int TC = 0; TC < TN; TC++) {
        ULL n;

        cin >> n;

        cout << "Case #" << (TC + 1) << ": " << solve(n) << endl;
    }
}

