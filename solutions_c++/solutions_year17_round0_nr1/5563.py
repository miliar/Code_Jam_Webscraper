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

void flip(string *str, int l, int k)
{
    string &s = *str;
    for (int i = l; i < l + k; ++i) {
        if (s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';
    }
}
int solve(string s, int k)
{
    int min = 0;
    int n = s.length();
    bool done = false;
    while (!done) {
        string prev = s;
        FOR(i, 0, n - k + 1) {
            if (s[i] == '-') {
                flip(&s, i, k);
                ++min;
            }
        }
        //for_each(ALL(s), [] (char c) { cout << c; });
        //cout << endl;
        done = true;
        FOR(i, 0, n) {
            if (s[i] == '-')
                done = false;
        }
        if (!done && prev == s) {
            min = -1;
            break;
        }
    }
    return min;
}
int main()
{
    int n;
    cin >> n;
    FOR(i, 0, n) {
        string s;
        getline(cin, s, ' ');
        int k;
        cin >> k;
        int min = solve(s, k);
        if (min < 0)
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i + 1 << ": " << min << endl;
    }
}
