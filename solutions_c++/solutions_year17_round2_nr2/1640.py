#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T; cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        int ma = max(r,max(y,b));
        if(ma > (r+y+b-ma)) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if(ma == r) {
            if(y > b) {
                while(r+y+b) {
                    if(r) { cout << 'R'; r--; }
                    if(y) { cout << 'Y'; y--; }
                    if((r == b-1) && b) { cout << 'B'; b--; }
                }
                cout << endl;
                continue;
            } else {
                while(r+y+b) {
                    if(r) { cout << 'R'; r--; }
                    if(b) { cout << 'B'; b--; }
                    if((r == y-1) && y) { cout << 'Y'; y--; }
                }
                cout << endl;
                continue;
            }
        } else if(ma == y) {
            if(r > b) {
                while(r+y+b) {
                    if(y) { cout << 'Y'; y--; }
                    if(r) { cout << 'R'; r--; }
                    if((y == b-1) && b) { cout << 'B'; b--; }
                }
                cout << endl;
                continue;
            } else {
                while(r+y+b) {
                    if(y) { cout << 'Y'; y--; }
                    if(b) { cout << 'B'; b--; }
                    if((y == r-1) && r) { cout << 'R'; r--; }
                }
                cout << endl;
                continue;
            }
        } else {
            if(r > y) {
                while(r+y+b) {
                    if(b) { cout << 'B'; b--; }
                    if(r) { cout << 'R'; r--; }
                    if((b == y-1) && y) { cout << 'Y'; y--; }
                }
                cout << endl;
                continue;
            } else {
                while(r+y+b) {
                    if(b) { cout << 'B'; b--; }
                    if(y) { cout << 'Y'; y--; }
                    if((b == r-1) && r) { cout << 'R'; r--; }
                }
                cout << endl;
                continue;
            }
        }
    }
    return 0;
}
