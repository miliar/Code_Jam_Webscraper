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
#include <random>
#include <chrono>

using namespace std;

typedef long double d64;

bool visited[1001][1001];
d64 saved_max[1001][1001];

pair<d64, d64> cakes[1001];

d64 getMaxIncrease(int start, int n, int k)
{
    if (!k)
        return 0;

    if (visited[start][k])
        return saved_max[start][k];

    visited[start][k] = true;

    d64 max_area = 0;
    for (int i = start; i < n; i++)
    {
        d64 R = cakes[i].first;
        d64 H = cakes[i].second;

        d64 cur_area = start == 0 ? R * R : 0;

        cur_area += 2 * R * H + getMaxIncrease(i + 1, n, k - 1);

        max_area = max(max_area, cur_area);
    }

    saved_max[start][k] = max_area;

    return saved_max[start][k];
}

d64 solve(int N, int K)
{
    sort(cakes, cakes + N);
    reverse(cakes, cakes + N);

    const d64 pi = acos(-1);

    return pi * getMaxIncrease(0, N, K);
}

void clean()
{
    for (int i = 0; i <= 1000; i++)
        for (int j = 0; j <= 1000; j++)
            visited[i][j] = false;
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
        int N, K;
        cin >> N >> K;

        for (int i = 0; i < N; i++)
            cin >> cakes[i].first >> cakes[i].second;

        cout << "Case #" << test_case << ": ";

        cout.precision(20);
        cout << fixed << solve(N, K) << '\n';

        clean();
    }
}