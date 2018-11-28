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

int r, c;
string scr[30];
bool colored[30];

bool rowColor(int i)
{
    char ch = '?';
    int st = 0;

    while (st < c)
    {
        int j;
        for (j = st; j < c; j++) {
            if (scr[i][j] != '?') {
                ch = scr[i][j];
                break;
            }
        }

        if (ch == '?') {
            if (st != 0) {
                cout << "why----------????????????????????????????\n";
            }
            return false;
        }

        for (j = st; j < c; j++) {
            if (scr[i][j] == '?') {
                scr[i][j] = ch;
            }
            else {
                ch = scr[i][j];
                j++;
                break;
            }
        }
        st = j;
    }

    return true;
}

/*_____________________________________________________________________________________*/

int main() {
    //*
    freopen("aa.in", "r", stdin);
    freopen("aa.out", "w", stdout);
    //*/
    int T;
    cin >> T;
    For1 (tc, T) {
        cerr << "--> " << tc << " / " << T << endl;
        cin >> r >> c;

        For(i, r) cin >> scr[i];

        For(i, r) {
            colored[i] = rowColor(i);
        }

        For (i, r) {
            if (colored[i]) continue;

            int rr = -1;
            for (int j = i - 1; j >= 0; j--)
            {
                if (colored[j]) {
                    rr = j;
                    break;
                }
            }
            if (rr == -1) {
                for (int j = i + 1; j < r; j++) {
                    if (colored[j]) {
                        rr = j;
                        break;
                    }
                }
            }

            if (rr == -1) {
                cout << "why2----------------------------------------------" << endl;
            }

            For(j, c) scr[i][j] = scr[rr][j];
        }

        cout << "Case #" << tc << ":\n";
        For(i, r) cout << scr[i] << endl;
    }

    return 0;
}
/*
?C?
D??
???
??F
*/
