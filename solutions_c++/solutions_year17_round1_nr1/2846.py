#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <map>
#include <utility>

#define FOR(i,n) for(int i=0;i<int(n);++i)

using namespace std;

using ull = unsigned long long;

int r,c;
char gr[30][30];


bool solve(int x, int y) {
    if (x >= r || y >= c) return true;
    
    // left
    char f = 0;
    int xx=x,yy=y;
    while ((gr[xx][y] == '?' || (!f && (f = gr[xx][y])) ) && xx < r) {
        xx++;
    }
    bool wrong = false;
    do {
        yy++;
        char f_ = f;
        for (int i=x; i<xx; ++i) {
            if (gr[i][yy] == '?' || (!f && (f = gr[i][yy]))) continue;
            wrong = true;
            break;
        }
       if (wrong) f = f_;
//        yy++;
    } while (yy < c && !wrong);
    
    assert(xx>x);
    assert(yy>y);
 
    char ff = 0;
    int xxx=x,yyy=y;
    while ((gr[x][yyy] == '?' || (!ff && (ff = gr[x][yyy])) ) && yyy < c) {yyy++;}
    wrong = false;
    do {
        xxx++;
        char f_ = ff;
        for (int i=y; i<yyy; ++i) {
            if (gr[xxx][i] == '?' || (!ff && (ff = gr[xxx][i]))) continue;
            wrong = true;
            break;
        }
        if (wrong) ff = f_;
//        xxx++;
    } while (xxx < r && !wrong);
    
    assert(xxx>x);
    assert(yyy>y);
    
    if ( ((xxx-x) * (yyy-y) < (xx-x)*(yy-y) && f > 0) || (f>0 && ff == 0)) {
        if (solve(x, yy) && solve(xx, y) && solve(xx, yy)) {
            for (int i=x;i<xx;++i) for (int j=y;j<yy;++j) {
                gr[i][j] = f;
            }
            return true;
        }
    }
        
    if (ff > 0 && solve(xxx, y) && solve(x, yyy) && solve(xxx, yyy)) {
        for (int i=x;i<xxx;++i) for (int j=y;j<yyy;++j) {
            gr[i][j] = ff;
        }
        return true;
    }
    
    return false;
}

void test() {
    cin >> r >> c;
    
    FOR(i, 30) FOR (j, 30) gr[i][j] = 0;
    FOR(i,r) FOR(j,c) cin >> gr[i][j];
    
    auto l = solve(0, 0);
    
    //cout << l << endl;
    cout << endl;
    FOR(i,r) {
        FOR(j,c) cout << gr[i][j];
        cout << endl;
    }
    
}

int main() {
    
    int tn; cin >> tn;
    FOR (t, tn) {
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
