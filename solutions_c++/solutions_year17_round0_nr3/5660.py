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

class Stall
{
public:
    bool isFree;
    int vLeft;
    int vRight;
    int minlr;
    int maxlr;
    bool operator <(Stall& r)
    {
        return (minlr != r.minlr ? minlr < r.minlr : maxlr < r.maxlr);
    }
};
Stall stall[sz];

int main() {
    //*
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    //*/
    int T;
    cin >> T;
    For1 (tc, T) {
        //cerr << "--> " << tc << " / " << T << endl;
        int n, k;
        cin >> n >> k;

        For (i, n) stall[i].isFree = true;

        int y = 0, z = 0;
        while (k--) {
            For (i, n) {
                if (stall[i].isFree) {
                    stall[i].vLeft = stall[i].vRight = 0;
                    for (int j = i - 1; j >= 0 && stall[j].isFree; j--) stall[i].vLeft++;
                    for (int j = i + 1; j < n && stall[j].isFree; j++) stall[i].vRight++;
                }
                stall[i].minlr = std::min(stall[i].vLeft, stall[i].vRight);
                stall[i].maxlr = std::max(stall[i].vLeft, stall[i].vRight);
            }
            int ind = -1;
            For (i, n) {
                if (stall[i].isFree == false) continue;
                if (ind == -1) ind = i;
                else if (stall[ind] < stall[i]) ind = i;
            }
            stall[ind].isFree = false;
            y = stall[ind].maxlr;
            z = stall[ind].minlr;
        }

        cout << "Case #" << tc << ": " << y << ' ' << z;
        cout << endl;
    }

    return 0;
}
/*

*/
