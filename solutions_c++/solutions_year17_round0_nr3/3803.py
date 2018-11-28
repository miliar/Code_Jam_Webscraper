#include <iostream>

using namespace std;

int large2pow(int lim) {
    int result = 1;
    while (lim > 1) {
        result *= 2;
        lim /= 2;
    }
    return result;
}

void getAnswer(int ansArr[2], int N, int K) {
    int pow2 = large2pow(K);
    int baseNum = (N - (pow2 - 1)) / pow2;
    int largeNumCnt = (N - (pow2 - 1)) % pow2;
    int order = K - pow2 - largeNumCnt;
    if (order < 0) {
        baseNum++;
    }
    if (baseNum == 0) {
        ansArr[0] = 0, ansArr[1] = 0;
    } else if (baseNum % 2 == 0) {
        ansArr[0] = baseNum / 2;
        ansArr[1] = baseNum / 2 - 1;
    } else {
        ansArr[0] = baseNum / 2;
        ansArr[1] = baseNum / 2;
    }
    return;
}

int main() {
    int testCase, N, K;
    int ansArr[2] = {0, };
    cin >> testCase;
    for (int i = 0; i < testCase; i++) {
        cin >> N >> K;
        getAnswer(ansArr, N, K);
        cout << "Case #" << i+1 << ": " << ansArr[0] << " " << ansArr[1] << endl;
        ansArr[0] = 0, ansArr[1] = 0;
    }
    return 1;
}