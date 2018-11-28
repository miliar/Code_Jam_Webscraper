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
/*_____________________________________________________________________________________*/

string cal(string str, int ind)
{
    if (ind < 1) {
        int k = str.length() - 1;
        str.clear();
        while (k--) str += '9';
        return str;
    }

    if ((ind > 1 && str[ind - 1] > str[ind - 2]) ||
            (ind == 1 && str[0] > '1')) {
        str[ind - 1]--;
        for (int i = ind; i < str.length(); i++) str[i] = '9';
        return str;
    }

    return cal(str, ind - 1);
}

int main() {
    //*
    freopen("bb.in", "r", stdin);
    freopen("bb.out", "w", stdout);
    //*/
    int T;
    cin >> T;
    For1 (tc, T) {
        cerr << "--> " << tc << " / " << T << endl;
        string str;
        cin >> str;

        int ind = -1;

        for (int i = 1; i < str.length(); i++)
        {
            if (str[i] < str[i - 1])
            {
                str = cal(str, i);
                break;
            }
        }

        cout << "Case #" << tc << ": " << str;
        cout << endl;
    }

    return 0;
}
/*
111111111111111110
99999999999999999
99999999999999999
*/
