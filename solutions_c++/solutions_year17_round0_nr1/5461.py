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

/*_____________________________________________________________________________________*/

// check debug, read 2 times (until full!)
// think --> idea? --> really works?

int main() {
    //*
    freopen("aa.in", "r", stdin);
    freopen("aa.out", "w", stdout);
    //*/
    int T;
    cin >> T;
    For1 (tc, T) {
        //cerr << "--> " << tc << " / " << T << endl;
        string str;
		int k;
		cin >> str >> k;

		int ans = 0;
		for (int i = 0; i <= str.length() - k; i++) {
			if (str[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++) {
					if (str[i + j] == '-') str[i + j] = '+';
					else str[i + j] = '-';
				}
			}
		}

		bool isGood = true;
		for (int i = 0; i < str.length(); i++) {
			if (str[i] == '-') isGood = false;
		}

        cout << "Case #" << tc << ": ";
		if (isGood) cout << ans;
		else cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}
/*

*/
