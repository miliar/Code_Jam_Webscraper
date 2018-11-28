#include <fstream>
#ifdef ONLINE_JUDGE
    #define cin in
    #define cout out
#endif
#include <algorithm>
#include <iostream>
//#include <cstdint>
#include <cstdio>
#include <set>
#include <string>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <map>
#include <queue>
#define int32_t int64_t
using namespace std;

const int32_t MAX = 123456 + 1;

const int32_t INF = 30000;

uint64_t gcd(uint64_t a, uint64_t b)
{
   return b ? gcd(b, a%b) : a;
}

bool comp(const pair<int32_t, int32_t> &a, const pair<int32_t, int32_t> &b) {
    return a.first * a.second > b.first * b.second;
}

void permute(vector<pair<int32_t, int32_t>> &pancakes) {

}

int main(int argc, char *argv[])
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    int32_t n, tests, k, i = 0;
    cin >> tests;
    for (int32_t t = 1; t <= tests; ++t) {
        cin >> n >> k;
        vector<pair<int32_t, int32_t>> pancake(n);
        for (int32_t i = 0; i < n; ++i)
            cin >> pancake[i].first >> pancake[i].second;
        sort(pancake.begin(), pancake.end(), std::greater<pair<int32_t, int32_t>>());
        double maxArea = 0;
        for (int32_t i = 0; i <= n - k; ++i) {
            // section 1
            vector<pair<int32_t, int32_t>>
                permuted(pancake.begin() + i + 1, pancake.end());
            stable_sort(permuted.begin(), permuted.end(), comp);
            double area = M_PI*pancake[i].first*pancake[i].first
                    + 2*M_PI*pancake[i].first*pancake[i].second;
            for (int32_t m = 0; m < k - 1; ++m) {
                area += 2*M_PI*permuted[m].first*permuted[m].second;
            }
            if (area > maxArea) maxArea = area;
        }

        cout << std::fixed << setprecision(9) <<  "Case #" << t << ": " << maxArea << endl;
    }

    return 0;
}
