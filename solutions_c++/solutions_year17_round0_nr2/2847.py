#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <functional>
#include <limits>
#include <queue>
#include <iomanip>
#include <deque>
#include <stack>
#include <cstdio>
#include <cmath>
#include <complex.h>
#include <cstdio>

using namespace std;

vector<int> get_digits(long long N)
{
    vector<int> digits;
    while (N)
    {
        digits.push_back(N % 10);
        N /= 10;
    }

    reverse(digits.begin(), digits.end());

    return digits;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

#ifndef ONLINE_JUDGE
    FILE *stream;
    freopen_s(&stream, "input.txt", "r", stdin);
    freopen_s(&stream, "output.txt", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        long long N;
        cin >> N;

        auto digits = get_digits(N);
        for (int i = digits.size() - 1; i < digits.size(); i--)
        {
            bool smaller_digit_exists = false;
            for (int j = i + 1; j < digits.size(); j++)
                smaller_digit_exists |= digits[j] < digits[i];

            if (smaller_digit_exists)
            {
                digits[i]--;
                for (int j = i + 1; j < digits.size(); j++)
                    digits[j] = 9;
            }
        }

        long long M = 0;
        for (int i = 0; i < digits.size(); i++)
        {
            M *= 10;
            M += digits[i];
        }

        cout << "Case #" << test_case << ": "
            << M
            << '\n';
    }
}