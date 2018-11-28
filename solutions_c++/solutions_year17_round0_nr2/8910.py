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

int n, numtest; 
string s;
int pos;

int tidy() {
	fto(i, 0, s.length() - 2) 
		if (s[i] > s[i + 1]) return i;
	return -1;
}

void print() {
	fto(i, 0, s.length() - 1) 
		if (s[i] != '0') {
			fto(j, i, s.length() - 1) cout << s[j];
			cout << endl;
			return;
		}
}

int main() {
	//#ifndef ONLINE_JUDGE
    	freopen("in.inp", "r", stdin);
    	freopen("ou1.out", "w", stdout);
    //#endif

    read(numtest); 
    fto(test, 1, numtest) {
    	read(s);

    	if (s.length() == 1) {
    		cout << "Case #" << test << ": " << s << endl;
    		continue;
    	}


    	while (1) {
    		pos = tidy();
    		if (pos == -1) {
    			cout << "Case #" << test << ": ";
    			print();
    			break;
    		}
    		s[pos]--;  //debug(s);
    		fto(i, pos + 1, s.length() - 1) s[i] = '9';
    	//	debug(s);
    	//	break;
    	}
    	
    }

 	//#ifndef ONLINE_JUDGE
  //  	cout << endl;
   // 	cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
	//#endif
}
