#pragma comment(linker, "/STACK:500000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <exception>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = static_cast<int>(2e9);

struct Pancake {
    int r, h;

    bool operator<(const Pancake& other) const {
        return r > other.r;
    }
} pancakes[1009];

bool cmp(Pancake& a, Pancake& b) {
    double s1 = 2 * PI * a.r * a.h;
    double s2 = 2 * PI * b.r * b.h;
    return s1 > s2;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
    int t;
    scanf("%d", &t);
    for (int test_number = 1; test_number <= t; ++test_number) {
        int n, k;
        scanf("%d %d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%d %d", &pancakes[i].r, &pancakes[i].h);
        }
        sort(pancakes, pancakes + n);
        double res = 0.0;
        for (int i = 0; i < n && n - i >= k; ++i) {
            double cur = 2 * PI * pancakes[i].r * pancakes[i].h + PI * pancakes[i].r * pancakes[i].r;
            sort(pancakes + i + 1, pancakes + n, cmp);
            for (int j = 1; j < k; ++j) {
                cur += 2 * PI * pancakes[i + j].r * pancakes[i + j].h;
            }
            sort(pancakes + i + 1, pancakes + n);
            res = max(res, cur);
        }
        printf("Case #%d: %.12lf\n", test_number, res);
    }
	return 0;
}