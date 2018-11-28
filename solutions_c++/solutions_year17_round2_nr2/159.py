#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#define _USE_MATH_DEFINES
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>
#include <iomanip>
#include <unordered_map>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))

#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cerr << "> " << #x << ": " << (x) << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

bool check(string result, int r, int o, int y, int g, int b, int v) {
    for (int i = 0; i < result.length(); ++i) {
        int i1 = i + 1;
        if (i1 == result.length()) i1 = 0;
        string forbidden;
        switch (result[i]) {
            case 'R':
                --r;
                forbidden = "VRO";
                break;
            case 'O':
                --o;
                forbidden = "VROYG";
                break;
            case 'Y':
                --y;
                forbidden = "OYG";
                break;
            case 'G':
                --g;
                forbidden = "OYGBV";
                break;
            case 'B':
                --b;
                forbidden = "GBV";
                break;
            case 'V':
                --v;
                forbidden = "GBVRO";
                break;
            default:
                throw result;
        }
        if (find(forbidden.begin(), forbidden.end(), result[i1]) != forbidden.end())
            return false;
    }
    if (r == 0 && o == 0 && y == 0 && g == 0 && b == 0 && v == 0)
        return true;
    throw result;
}

string calc(int r, int o, int y, int g, int b, int v) {
    int n = r + o + y + g + b + v;
    if (o > b || o > 0 && o == b && o + b != n) return string();
    if (g > r || g > 0 && g == r && g + r != n) return string();
    if (v > y || v > 0 && v == y && v + y != n) return string();
    if (r - g > b - o + y - v || y - v > r - g + b - o || b - o > r - g + y - v) return string();
    char last = 'a';
    string result;
    int prev = r + o + y + g + b + v;
    while (r > 0 || y > 0 || b > 0) {
        int ch = 0;
        int ch1 = 0;
        if (last != 'R') ch = max(ch, r - g);
        if (last != 'Y') ch = max(ch, y - v);
        if (last != 'B') ch = max(ch, b - o);
        if (r > 0 && last != 'R' && r - g >= ch && (result.length() == 0 || result[0] == 'R' || result[0] == last || r - g > y - v && r - g > b - o)) {
            result.push_back('R');
            --r;
            while (g > 0) {
                result.push_back('G');
                --g;
                if (r > 0) {
                    result.push_back('R');
                    --r;
                } else {
                    assert(result.length() == n && result[0] == 'R');
                }
            }
            last = 'R';
        }
        if (y > 0 && last != 'Y' && y - v >= ch && (result.length() == 0 || result[0] == 'Y' || result[0] == last || y - v > r - g && y - v > b - o)) {
            result.push_back('Y');
            --y;
            while (v > 0) {
                result.push_back('V');
                --v;
                if (y > 0) {
                    result.push_back('Y');
                    --y;
                } else {
                    assert(result.length() == n && result[0] == 'Y');
                }
            }
            last = 'Y';
        }
        if (b > 0 && last != 'B' && b - o >= ch && (result.length() == 0 || result[0] == 'B' || result[0] == last || b - o > r - g && b - o > y - v)) {
            result.push_back('B');
            --b;
            while (o > 0) {
                result.push_back('O');
                --o;
                if (b > 0) {
                    result.push_back('B');
                    --b;
                } else {
                    assert(result.length() == n && result[0] == 'B');
                }
            }
            last = 'B';
        }
        if (prev == r + o + y + g + b + v) {
            cerr << result << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << " " << last << endl;
            throw 1;
        }
        prev = r + o + y + g + b + v;
    }
    assert(r == 0 && o == 0 && y == 0 && g == 0 && b == 0 && v == 0);
    return result;
}

string calc_slow(int r, int o, int y, int g, int b, int v) {
    string result;
    for (int i = 0; i < r; ++i) {
        result.push_back('r');
    }
    for (int i = 0; i < o; ++i) {
        result.push_back('o');
    }
    for (int i = 0; i < y; ++i) {
        result.push_back('y');
    }
    for (int i = 0; i < g; ++i) {
        result.push_back('g');
    }
    for (int i = 0; i < b; ++i) {
        result.push_back('b');
    }
    for (int i = 0; i < v; ++i) {
        result.push_back('v');
    }
    std::transform(result.begin(), result.end(),result.begin(), ::toupper);
    sort(result.begin(), result.end());
    do {
        if (check(result, r, o, y, g, b, v))
            return result;
    } while (next_permutation(result.begin(), result.end()));
    return string();
}


void start_testing() {
    for (int n = 1; n < 1000; ++n) {
        for (int r = 0; r <= n; ++r) {
            for (int o = 0; o <= n - r; ++o) {
                for (int y = 0; y <= n - r - o; ++y) {
                    for (int g = 0; g <= n - r - o - y; ++g) {
                        for (int b = 0; b <= n - r - o - y - g; ++b) {
                            int v = n - r - o - y - g - b;
                            auto result_fast = calc(r, o, y, g, b, v);
                            if (result_fast.length() != 0 && !check(result_fast, r, o, y, g, b, v)) {
                                cerr << "Wrong: " << result_fast << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
                                break;
                            }
                            // auto result_slow = calc_slow(r, o, y, g, b, v);
                            // if (result_slow.length() == 0) {
                            //     if (result_fast.length() != 0) {
                            //         if (check(result_fast, r, o, y, g, b, v)) {
                            //             cerr << "Cannot be success: " << result_fast << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
                            //             break;
                            //         } else {
                            //             cerr << "Wrong: " << result_fast << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
                            //             break;
                            //         }
                            //     }
                            // } else {
                            //     if (result_fast.length() != 0) {
                            //         if (!check(result_fast, r, o, y, g, b, v)) {
                            //             cerr << "Wrong: " << result_fast << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
                            //             break;
                            //         }
                            //     } else {
                            //         cerr << "Could not find: " << result_slow << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
                            //         break;
                            //     }
                            // }
                        }
                    }
                }
            }
        }
        cout << "n = " << n << ": OK" << endl;
    }
}


int main() {
     // freopen("../input.txt", "rt", stdin);
     // freopen("../output.txt", "wt", stdout);

    // start_testing();

    int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n;
        int r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        auto res = calc(r, o, y, g, b, v);
        if (res.length() == 0)
            res = "IMPOSSIBLE";
        // printf("Case #%d: %.7f\n", testNumber, res);
        printf("Case #%d: %s\n", testNumber, res.c_str());
        // cout << "Case #" << testNumber << ": " << setprecision(6) << res << endl;
    }

    return 0;
}
