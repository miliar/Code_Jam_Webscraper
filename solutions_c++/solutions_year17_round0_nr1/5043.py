#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <queue>
#include <set>
using namespace std;
#define rep(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define rep1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define db(x) {cout << #x << " = " << (x) << endl;}
#define dba(a, x, y) {cout<<#a<<" :";FOR(i123,x,y)cout<<setw(4)<<(a)[i123];cout<<endl;}
#define clr(x) memset(x,0,sizeof(x));
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())

int SideUp(string s, int k) {
    int flips = 0;
    int n = s.length();
    FOR(i, 0, n - k)
        if (s[i] == '-') {
            rep(j, k)
                s[i + j] = ( s[i + j] == '-' ? '+' : '-' );
            flips++;
        }

    FOR(i, n - k + 1, n - 1)
        if (s[i] == '-')
            return -1;
    return flips;
}

int main() {
    int t;
    cin >> t;

    string pancakes;
    int k;
    int result;
    rep1(Yo, t) {
        cin >> pancakes;
        cin >> k;
        result = SideUp(pancakes, k);
        if (result < 0)
            cout << "Case #" << Yo << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << Yo << ": " << result << endl;
    }

    return 0;
}
