// In the Name of Allah
// AD13

#include <set>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;		//	typedef unsigned long long  ull;
typedef pair <int, int> pii;//	typedef pair <double, double> pdd;
#define MP make_pair
const int INF = 2147483647, MOD = 1000*1000*1000 + 7;
const double eps = 1e-8; // (eps < 1e-15) is the fact (1e-14)
#define For(i, n) for (int i = 0; i < (n); i++)
#define For1(i, n) for (int i = 1; i <= (n); i++)
//#define debug(x) { cerr << #x << " = _" << (x) << "_" << endl; }
void Error(string err) { cout << err; cerr << "_" << err << "_"; exit(0); }
int gcd(int a, int b) { return (b==0)? a: gcd(b, a%b); }
/*-------------------------------------------------------------------------------------*/

const int sz = 100 * 1000;

enum Col
{
    R = 0,
    O,
    Y,
    G,
    B,
    V
};
string colorStrs = "ROYGBV";

int main() {
    //*
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    //*/
    int T;
    cin >> T;
    For1 (tc, T) {
        //cerr << "--> " << tc << " / " << T << endl;

        // red , yellow , blue  -  R, Y, B   O, G, V
        // 1 -> 1
        // red and yellow -> orange O
        // yellow and blue -> green G
        // red and blue -> violet V

        int n; cin >> n;

        int colors[10];
        For(i, 6) cin >> colors[i];

        string ans;

        bool pos = true;
        if (colors[R] > colors[Y] + colors[B]) pos = false;
        if (colors[Y] > colors[R] + colors[B]) pos = false;
        if (colors[B] > colors[Y] + colors[R]) pos = false;

        if (pos == false) ans = "IMPOSSIBLE";
        else {
            int turn = R;
            if (colors[Y] < colors[turn]) turn = Y;
            if (colors[B] < colors[turn]) turn = B;
            char last = colorStrs[turn];
            int bad = turn;
            while (n--) {
                if (last == 'R') { turn = (colors[Y] > colors[B]) ? Y : B; if(colors[Y] == colors[B] && bad == B) turn = Y; }
                if (last == 'Y') { turn = (colors[R] > colors[B]) ? R : B; if(colors[R] == colors[B] && bad == B) turn = R; }
                if (last == 'B') { turn = (colors[R] > colors[Y]) ? R : Y; if(colors[R] == colors[Y] && bad == Y) turn = R; }
                last = colorStrs[turn];
                ans += last;
                colors[turn]--;
            }
        }

        cout << "Case #" << tc << ": " << ans;
        cout << endl;
    }

    return 0;
}
/*

*/
