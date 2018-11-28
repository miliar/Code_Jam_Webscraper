//AnotherHackyCodeBySmartCoder
//TidyNumbers.cpp
//Apr 8, 2017
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>());
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi = acos(-1.0);
const double eps = 1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
void fastIO() {
	std::ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
}

ll MAXN;
int tc;
ll gen(ll n) {
	if (n > MAXN)
		return 0;
	ll res = n;
	for (int i = max(1ll, n % 10); i <= 9 && n * 10 + i <= MAXN; i++)
		res = max(res, gen(n * 10 + i));
	return res;
}
int main() {
	fastIO();
    freopen("B-large.out","w",stdout);
	freopen("B-large.in", "r", stdin);

	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		cin >> MAXN;
		cout << "Case #" << t << ": " << gen(0);
		if (t != tc)
			cout << endl;
	}

	return 0;
}
