#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int INF = 1000 * 1000 * 1000 + 11;
const ll LINF = (ll)INF * INF;
const ld EPS = 1e-9;


const string FAIL = "IMPOSSIBLE";

string make_simple(int N, char a, char b) {
    string ret;
    for (int i = 0; i != N; ++i) {
        ret += a;
        ret += b;
    }
    return ret;
}

string make_group(int N, int ADD, char a, char b) {
    assert(N > ADD);
    
    string ret;
    for (int i = 0; i != N + ADD; ++i) {
        if (i % 2 == 0) ret += a;
        ret += b;
    }
    return ret;
}


struct Group {
    int N, A;
    char a, b;
    
    Group(int N, int A, char a, char b) : N(N), A(A), a(a), b(b) {
        assert(A == 0 || N > A);
    }
    
    int value() const {
        return N - A;
    }
    
    bool operator<(Group const &g) const {
        return value() > g.value();
    }
    
    string print() {
        assert(value());
        
        if (!A) {
            --N;
            return string(1, a);
        }
        
        string res;
        for (int i = 0; i != 2 * A + 1; ++i) {
            res += i % 2 ? b : a;
        }
        N -= A + 1;
        A = 0;
        return res;
    }
};


bool check(int N, int R, int O, int Y, int G, int B, int V, const string &str) {
    if (str.length() != N) return false;
    if (count_if(str.begin(), str.end(), [](char ch){ return ch == 'R'; }) != R) return false;
    if (count_if(str.begin(), str.end(), [](char ch){ return ch == 'O'; }) != O) return false;
    if (count_if(str.begin(), str.end(), [](char ch){ return ch == 'Y'; }) != Y) return false;
    if (count_if(str.begin(), str.end(), [](char ch){ return ch == 'G'; }) != G) return false;
    if (count_if(str.begin(), str.end(), [](char ch){ return ch == 'B'; }) != B) return false;
    if (count_if(str.begin(), str.end(), [](char ch){ return ch == 'V'; }) != V) return false;
    
    static const map<char, set<char>> allowed = {
        {'R', {'Y', 'B', 'G'}},
        {'Y', {'R', 'B', 'V'}},
        {'B', {'R', 'Y', 'O'}},
        {'O', {'B'}},
        {'G', {'R'}},
        {'V', {'Y'}},
    };
    
    for (int i = 0; i != str.size() - 1; ++i) {
        if (!allowed.at(str[i]).count(str[i + 1])) return false;
    }
    if (!allowed.at(str[0]).count(str.back())) return false;
    
    return true;
}

set<string> stupid(int N, int R, int O, int Y, int G, int B, int V) {
    string p;
    p += string(R, 'R');
    p += string(O, 'O');
    p += string(Y, 'Y');
    p += string(G, 'G');
    p += string(B, 'B');
    p += string(V, 'V');
    
    sort(p.begin(), p.end());
    
    set<string> res;
    do {
        if (check(N, R, O, Y, G, B, V, p)) res.insert(p);
    } while (next_permutation(p.begin(), p.end()));
    
    return res;
}


// RY = O, YB = G, RB = V
string solve(int N, int R, int RY, int Y, int YB, int B, int RB) {
    if (B == RY && N == B + RY) {
        return make_simple(N / 2, 'B', 'O');
    }
    if (RY && B <= RY) return FAIL;
    if (R == YB && N == R + YB) {
        return make_simple(N / 2, 'R', 'G');
    }
    if (YB && R <= YB) return FAIL;
    if (Y == RB && N == Y + RB) {
        return make_simple(N / 2, 'Y', 'V');
    }
    if (RB && Y <= RB) return FAIL;
    
    vector<Group> groups;
    groups.emplace_back(R, YB, 'R', 'G');
    groups.emplace_back(Y, RB, 'Y', 'V');
    groups.emplace_back(B, RY, 'B', 'O');
    
    sort(groups.begin(), groups.end());
    
    int cnt = groups[0].value() + groups[1].value() + groups[2].value();
    if (groups[0].value() > cnt / 2) return FAIL;
    
    int lastSecond = 2;
    vector<string> res(cnt);
    
    for (int i = 0; i < cnt; i += 2) {
        for (int j = 0; j != 3; ++j) {
            if (groups[j].value()) {
                res[i] = groups[j].print();
                break;
            }
        }
    }
    
    for (int i = 1; i < cnt; i += 2) {
        for (int j = 0; j != 3; ++j) {
            if (groups[j].value()) {
                res[i] = groups[j].print();
                break;
            }
        }
    }
    
    string res_str;
    for (auto const &str : res) {
        res_str += str;
    }
    
    assert(check(N, R, RY, Y, YB, B, RB, res_str));
    
    return res_str;
}

void test(int N, int R, int O, int Y, int G, int B, int V) {
    auto a = solve(N, R, O, Y, G, B, V);
    auto b = stupid(N, R, O, Y, G, B, V);
    
    if ((a == FAIL && !b.empty()) || (a != FAIL && !b.count(a))) {
        cout << N << ' ' << R << ' ' << O << ' ' << Y << ' ' << G << ' ' << B << ' ' << V << '\n';
        cout << a << '\n';
        cout << (b.empty() ? FAIL : *(b.begin())) << '\n';
        exit(0);
    }
}


void stress() {
    for (int i = 0; i != 10000;) {
        cout << i << '\r';
        cout.flush();
        
        int R = rand() % 10;
        int Y = rand() % 10;
        int B = rand() % 10;
        int O = rand() % 5;
        int G = rand() % 5;
        int V = rand() % 5;
        
        int N = R + Y + B + O + G + V;
        if (N < 3 || N > 10) continue;
        ++i;
                            
        test(N, R, Y, B, O, G, V);
    }
    
    cout << "OK\n";
}


int main() {
    // stress();
    // return 0;
    
    ios_base::sync_with_stdio(false);
    // cin.tie(0);
    
    cout.precision(20);
    cout << fixed;
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << test + 1 << ": " << solve(N, R, O, Y, G, B, V) << "\n";
    }
    
    return 0;
}