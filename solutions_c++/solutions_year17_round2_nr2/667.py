//#define _GLIBCXX_DEBUG
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>
#include <gmpxx.h>
#include <tuple>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 
typedef mpz_class bint;

template<typename T>
string toS(const T &d) {
    ostringstream oss;
    oss << d;
    return oss.str();
}

#define COLOR_R 0
#define COLOR_Y 1
#define COLOR_B 2

set<tuple<int, int, int, int> > mem;

bool solve(string &s, int start, int last, int r, int y, int b) {
    if (r > y+b+2) return false;
    if (y > r+b+2) return false;
    if (b > r+y+2) return false;
    tuple<int, int, int, int> key{last, r, y, b};
    if (mem.find(key) != mem.end())
        return false;
    mem.insert(key);
    if (r+y+b == 1) {
        if (r == 1) {
            if (start == COLOR_R || last == COLOR_R)
                return false;
            else {
                s += 'R';
                return true;
            }
        }
        else if (y == 1) {
            if (start == COLOR_Y || last == COLOR_Y)
                return false;
            else {
                s += 'Y';
                return true;
            }
        }
        else {
            assert(b == 1);
            if (start == COLOR_B || last == COLOR_B)
                return false;
            else {
                s += 'B';
                return true;
            }
        }
    }
    if (r > 0 && last != COLOR_R) {
        s += 'R';
        if (solve(s, start, COLOR_R, r-1, y, b))
            return true;
        s.pop_back();
    }
    if (y > 0 && last != COLOR_Y) {
        s += 'Y';
        if (solve(s, start, COLOR_Y, r, y-1, b))
            return true;
        s.pop_back();
    }
    if (b > 0 && last != COLOR_B) {
        s += 'B';
        if (solve(s, start, COLOR_B, r, y, b-1))
            return true;
        s.pop_back();
    }
    return false;
}

string solve(int N, int R, int O, int Y, int G, int B, int V)
{
    assert(N == R+O+Y+G+B+V);
    assert(O+G+V == 0);
    mem.clear();
    if (R) {
        string ans = "R";
        if (solve(ans, COLOR_R, COLOR_R, R-1, Y, B))
            return ans;
    }
    else if (Y) {
        string ans = "Y";
        if (solve(ans, COLOR_Y, COLOR_Y, R, Y-1, B))
            return ans;
    }
    else {
        assert(B > 0);
        string ans = "B";
        if (solve(ans, COLOR_B, COLOR_B, R, Y, B-1))
            return ans;
    }
    
    return "IMPOSSIBLE";
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << _t+1 << ": " << solve(N, R, O, Y, G, B, V) << endl;
    }

    return 0;
}
