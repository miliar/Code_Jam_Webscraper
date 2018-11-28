#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <numeric>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define showv(v) For(i, v) { cout << *i << ' ';} cout << endl;
#define maxv(v) *max_element(all(v))
#define minv(v) *min_element(all(v))

typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef vector<vector<char> > vcc;
typedef vector<bool> vb;
typedef vector<long long> vll;
typedef long long ll;
typedef long double ld;

void solve(ll stalls, int times) {

	int adj, split = 0;
	ll L = 0, R = stalls, current;
	vll all, buff;
	all.pb(stalls);
	while (split <= times) {
			
		For(it, all) {
			current = *it;
			adj = (current%2==0) ? 1 : 0;
			R = current >> 1;
			buff.pb(R);
			buff.pb(fmax(0, R - adj));
			// cout << "R: " << R << "\tL: " << fmax(0, R - adj) << endl;
			split++;
			if (split==times) goto imdone;
			// cout << "Split: " << split << " Times: " << times << endl;
		}
		all = buff;
		sort(all(all), greater<ll>());
		buff.clear();
	}

	imdone:;
	L = fmax(0, R - adj);
	// cout << L << ' ' << R << endl;

    cout << fmax(L,R) << ' ' << fmin(L,R) << endl;
}

int N;
int main(int argc, char *args[]) {
	if (argc == 2 && strcmp(args[1], "small") == 0) {
		freopen("small.in","rt",stdin);
		freopen("small.out","wt",stdout);
	}
	else if (argc == 2 && strcmp(args[1], "large") == 0) {
		freopen("large.in","rt",stdin);
		freopen("large.out","wt",stdout);
	}
	else {
		freopen("test-in.txt", "rt", stdin);
		freopen("test-out.txt", "wt", stdout);
	}
	
	cout << setprecision(0) << fixed;
	cin>>N;
	rep2(nn,1,N+1) {
		printf("Case #%d: ", nn);

		ll stalls, K; cin >> stalls >> K;
		solve(stalls, K);

	}
	
	return 0;
}