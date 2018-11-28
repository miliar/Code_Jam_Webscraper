#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <climits>
#include <string>
using namespace std;

typedef long long ll;

string solve(int n, int r, int o, int y, int g, int b, int v)
{
    string res = "";
    if (r > 0 && r >= b && r >= y) {
        r--;
        res += "R";
    } else if (b > 0 && b >= r && b >= y) {
        b--;
        res += "B";
    } else if (y > 0 && y >= r && y >= b) {
        y--;
        res += "Y";
    }
        
    while (r > 0 || b > 0 || y > 0) {
        char last = res[res.size()-1];
        //cerr << r << ' '<< b << ' ' << y << ' ' << last << ' ' << res << endl;
        if (last == 'R') {
            if (b > 0 && b >= y) {
                res += "B";
                b--;
            } else if (y > 0 && y >= b) {
                res += "Y";
                y--;
            } else {
                return "IMPOSSIBLE";
            }
        } else if (last == 'B') {
            if (r > 0 && r >= y) {
                res += "R";
                r--;
            } else if (y > 0 && y >= r) {
                res += "Y";
                y--;
            } else {
                return "IMPOSSIBLE";
            }
        } else if (last == 'Y') {
            if (b > 0 && b >= r) {
                res += "B";
                b--;
            } else if (r > 0 && r >= b) {
                res += "R";
                r--;
            } else {
                return "IMPOSSIBLE";
            }
        }
    }
    char last = res[res.size()-1];
    if (res[0] == last) {
        // try swapping last 2 unicorns
        if (last != res[res.size()-3]) {
            res[res.size()-1] = res[res.size()-2];
            res[res.size()-2] = last;
        } else {
            return "IMPOSSIBLE";
        }
    }
    return res;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << cas << ": " << solve(n, r, o, y, g, b, v) << endl;
    }
}
