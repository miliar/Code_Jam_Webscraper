#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, T, r, o, y, g, b, v;

void draw(string &ans, char c) {
    ans += c;
    if (c == 'R') {
        r--;
        while (g > 0) {
            ans += "GR";
            g--;
        }
    }
    if (c == 'Y') {
        y--;
        while (v > 0) {
            ans += "VY";
            v--;
        }
    }
    if (c == 'B') {
        b--;
        while (o > 0) {
            ans += "OB";
            o--;
        }
    }
}

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        printf("Case #%d: ", id);
        cin >> n >> r >> o >> y >> g >> b >> v;
        if (r < g || y < v || b < o || (r > 0 && r == g && r + g < n) || (y > 0 && y == v && y + v < n) || (b > 0 && b == o && b + o < n)) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        r -= g;
        y -= v;
        b -= o;

        int s = r + y + b;
        if (r + r > s || y + y > s || b + b > s) {
            printf("IMPOSSIBLE\n");
            continue;
        }

        bool clip = false;
        if ((r == 0 && g > 0) || (y == 0 && v > 0) || (b == 0 && o > 0)) {
            clip = true;
            if (g > 0) r++;
            if (v > 0) y++;
            if (o > 0) b++;
        }

        string ans;
        char last = ' ', ch, first = 'R';
        while (r + y + b > 0) {
            if (r >= y && r >= b && !((r == y && first == 'Y' || r == b && first == 'B'))) {
                if (last != 'R') ch = 'R';
                else if (y > b || (y == b && first == 'Y')) ch = 'Y';
                else ch = 'B';
            }
            else if (y >= r && y >= b && !((y == r && first == 'R' || y == b && first == 'B'))) {
                if (last != 'Y') ch = 'Y';
                else if (r > b || (r == b && first == 'R')) ch = 'R';
                else ch = 'B';
            }
            else if (b >= r && b >= y && !((b == r && first == 'R' || b == y && first == 'Y'))) {
                if (last != 'B') ch = 'B';
                else if (r > y || (r == y && first == 'R')) ch = 'R';
                else ch = 'Y';
            }
            if (ans.length() == 0) first = ch;
            draw(ans, ch);
            last = ch;
        }
        if (clip) ans = ans.substr(1);
        if (ans[0] == ans[n - 1]) printf("IMPOSSIBLE\n");
        else printf("%s\n", ans.c_str());
    }
}
