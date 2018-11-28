#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

#define For(i, n) for(int i = 0; i < (n); i++)

bool setc (string& res, char c, int& x, int rc, int bc, int yc) {
    if (x >= rc && x >= bc && x >= yc) {
        --x;
        res += c;
        return true;
    }

    return false;
}

string solve(int n, int r, int b, int y, int o, int g, int v) {
    if (r > n / 2 || b > n / 2 || y > n / 2)
        return "IMPOSSIBLE";

    string res = "";
    int rc = r;
    int bc = b;
    int yc = y;

    if (setc(res, 'R', rc, rc, bc, yc)) { }
    else if (setc(res, 'B', bc, rc, bc, yc)) { }
    else if (setc(res, 'Y', yc, rc, bc, yc)) { }
    
    For (i, n - 1) {
        if (res.back() == 'R') {
            if (bc > yc || (bc == yc && b >= y)) 
                res += 'B', bc--;
            else
                res += 'Y', yc--;
        }
        else if (res.back() == 'B') {
            if (rc > yc || (rc == yc && r >= y)) 
                res += 'R', rc--;
            else
                res += 'Y', yc--;
        }
        else if (res.back() == 'Y') {
            if (bc > rc || (bc == rc && b >= r)) 
                res += 'B', bc--;
            else
                res += 'R', rc--;
        }
    }

    // For (i, n) {
    //     if (res[i] == res[(i + 1) % n])
    //         cerr << "FAILED: " << res << endl;
    //     if (res[i] == res[(i - 1 + n) % n])
    //         cerr << "FAILED: " << res << endl;
    // }

    return res;
}

int main () {
    int t;
    scanf("%d", &t);

    For (i, t) {
        int n, r, b, y, o, g, v;

        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);      
        printf("Case #%i: %s\n", i + 1, (solve(n, r, b, y, o, g, v)).c_str());
    }
}