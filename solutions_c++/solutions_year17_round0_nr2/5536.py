#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

template<typename T>
using mat = vector<vector<T>>;

template<typename T>
using lim = numeric_limits<T>;

#define mod 1000000007
#define f first
#define s second
#define ALL(x) (x).begin(), (x).end()
#define RFOR(i, a, n) for (int64_t i = (a - 1); i >= (n); --i)
#define FOR(i, a, n) for (int64_t i = (a); i < (n); ++i)
#define pb push_back
#define nx_perm next_permutation
#define sz size
#define PI 3.14159265358979323846264
/****************************************/

bool is_tidy(long num)
{
    long t = 9;
    while (num) {
        int n = t;
        t = num % 10;
        if (t > n){
            return false;
        }
        num /= 10;
    }
    return true;
}
long solve(long r)
{
    if (r < 10)
        return r;
    string s(to_string(r));
    while (!is_tidy(stoul(s))) {
        RFOR(i, s.sz(), 1) {
            if (s[i - 1] > s[i]) {
                FOR(j, i, (int) s.sz()) {
                    s[j] = '9';
                }
                --s[i - 1];
            }
        }

    }
    return stoul(s);
}

int main()
{
    int n;
    cin >> n;
    FOR(i, 0, n) {
        long t;
        cin >> t;
        long min = solve(t);

        cout << "Case #" << i + 1 << ": " << min << endl;
    }
}
