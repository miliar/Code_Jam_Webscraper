#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        string pancakes;
        int K, ans = 0, i = 0, N;

        cin >> pancakes;
        cin >> K;

        N = pancakes.length();

        while (pancakes[i] == '+' && i < N) {
            i++;
        }

        if (i < N) {
            while (i < N - K + 1) {
                // Flip K pancakes
                for (int j = i; j < i + K; ++j) {
                    if (pancakes[j] == '+') {
                        pancakes[j] = '-';
                    } else {
                        pancakes[j] = '+';
                    }
                }

                ans++;

                while (pancakes[i] == '+' && i < N) {
                   i++;
                }
            }
        }

        if (i == N) {
            printf("Case #%d: %d\n", t, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
    }

    return 0;
}
