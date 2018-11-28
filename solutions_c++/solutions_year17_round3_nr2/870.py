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

const int sz = 1000;

struct MyTask
{
    int st;
    int end;
};

MyTask tc[sz];
MyTask tj[sz];

/*_____________________________________________________________________________________*/

// think --> idea? --> really works?

int main() {
    //*
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    //*/
    int T;
    cin >> T;
    For1 (tc1, T) {
        //cerr << "--> " << tc << " / " << T << endl;
        int ac, aj;
        cin >> ac >> aj;

        For(i, ac) cin >> tc[i].st >> tc[i].end;
        For(i, aj) cin >> tj[i].st >> tj[i].end;

        int ans = 2;

        if (ac + aj > 1 && ac != 1) {
            MyTask* t = tc;
            if (aj == 2) {
                t = tj;
            }

            int st0 = t[0].st, st1 = t[1].st;
            int en0 = t[0].end, en1 = t[1].end;
            if (st0 > st1) {
                swap(st0, st1);
                swap(en0, en1);
            }

            int thresh = 12 * 60;
            if ((st1 - en0 < thresh) && (2 * thresh - en1 + st0 < thresh)) ans = 4;
        }

        cout << "Case #" << tc1 << ": " << ans;
        cout << endl;
    }

    return 0;
}
/*

*/
