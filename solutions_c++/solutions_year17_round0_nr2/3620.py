// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;

const int MAX_N = (int)3e5 + 5;

string n;
string res;

string lastTidyNumber() {
    cin >> n;
    res = "";
    for (int i = 0; i < sz(n); i++) {
        bool good = 1;
        for (int j = i; j < sz(n); j++) {
            if (n[j] < n[i]) {
                good = 0;
                break;
            }
            else if (n[j] > n[i])
                break;
        }
        if (good)
            res += n[i];
        else {
            res += char(n[i] - 1);
            for (int j = i + 1; j < sz(n); j++)
                res += "9";
            break;
        }
    }
    while(res[0] == '0')
        res.erase(res.begin());
    return res;
}

bool bad(int x) {
    string s = "";
    while(x) {
        s += char(x % 10 + '0');
        x /= 10;
    }
    for (int i = 0; i + 1 < sz(s); i++)
        if (s[i] < s[i + 1])
            return 1;
    return 0;
}

int calc() {
    int N = 0;
    for (auto i : n)
        N = N * 10 + i - '0';
    while(bad(N))
        N--;
    return N;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base :: sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int numberOfTests;
    cin >> numberOfTests;
    for (int testIndex = 1; testIndex <= numberOfTests; testIndex++) {
        cout << "Case #" << testIndex << ": " << lastTidyNumber() << endl;
    }
    return 0;
}
