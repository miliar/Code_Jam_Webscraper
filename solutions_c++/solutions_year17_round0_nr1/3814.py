#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void flip(string& S, int position, int K) {
    for (int i = position; i < position + K; i++) {
        if (S[i] == '+') {
            S[i] = '-';
        } else {
            S[i] = '+';
        }
    }
}

int solve(string& S, int K) {
    int L = S.size();

    int res = 0;
    for (int i = 0; i < L; i++) {
        if (S[i] == '-') {
            if (i + K - 1 >= L) {
                // flip not possible, reached end
                return -1;
            } 
            // flip
            flip(S, i, K);
            res++;
        }
    }

    return res;
}

int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; c++) {
        string S;
        int K;
        cin >> S >> K;
       
        int res = solve(S, K);

        if (res >= 0) {
            printf("Case #%d: %d\n", c, res);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", c);
        }
    }

    return 0;
}