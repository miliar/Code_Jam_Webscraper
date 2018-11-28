// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

#define fto(i,a,b) for (int i = (a); i <= b; i++)
#define fdw(i,a,b) for (int i = (a); i >= b; i--)
#define rep(i,a) for(int i = 0; i < a; i++) 
#define read(a) cin >> a
#define read2(a, b) cin >> a >> b
#define read3(a, b, c) cin >> a >> b >> c
#define read4(a, b, c, d) cin >> a >> b >> c >> d
#define write(a) cout << a << " "
#define writeln(a) cout << a << "\n"

#define PI 3.14159265
#define oo 1000000000
#define debug(a) cout << #a << " = " << a << endl

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;

#define maxn 100005

using namespace std;

string s;
int n, k, res, resnow, numtest, x[maxn];

bool check() {
	resnow = 0;
	fto(i, 0, n - k) {
		if (x[i] == 1) {
			resnow++;
			fto(j, i, i + k - 1)
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
		}
	}

	//debug(s);

	bool ok = true;
	fto(i, 0, s.length() - 1) 
		if (s[i] == '-') {
			ok = false;
			break;
		}

	fto(i, 0, n - k + 1) {
		if (x[i] == 1) {
			fto(j, i, i + k - 1)
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
		}
	}		

	return ok;
}

void brute(int i) {
	if (i > n - k) {
		if (check() && res > resnow) res = resnow;
		return;
	}
	fto(j, 0, 1) {
		x[i] = j;
		brute(i + 1);
	}
}

int main() {
	//#ifndef ONLINE_JUDGE
    	freopen("in.inp", "r", stdin);
    	freopen("ou.out", "w", stdout);
   // #endif

    read(numtest);
    fto(test, 1, numtest) {
    	read(s);  read(k); // debug(k);
    	n = s.length();

    	res = oo;
    	fto(i, 0, s.length() - 1) x[i] = 0;
    	brute(0);
    	if (res == oo) cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    	else cout << "Case #" << test << ": " << res << endl;
    }

 	//#ifndef ONLINE_JUDGE
    //	cout << endl;
    //	cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
	//#endif
}
