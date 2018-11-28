
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------

#ifdef cin fin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif



int main() {
	ios::sync_with_stdio(0);
	int t, z = 1;
	cin >> t;
	while(t--){
		cout << "Case #" << z++ << ": ";
		ll n, k;
		cin >> n >> k;
		map<ll, ll> m;
		m[n] = 1;
		while (true){
			ll x = m.rbegin()->first - 1, cnt = m.rbegin()->second;
			m.erase((--m.end())->first);
			if(k <= cnt){
				cout << x / 2 + x % 2 << " " << x / 2 << endl;
				break;
			}
			k -= cnt;
			m[x / 2] += cnt;
			m[x / 2 + x % 2] += cnt;
		}
	}
	return 0;
}