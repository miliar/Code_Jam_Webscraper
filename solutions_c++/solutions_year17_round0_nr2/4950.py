#include "io.h"

/***************************** START COPY ************************************/

#include "bits/stdc++.h"
using namespace std;

#define forn(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define forn1(i, n) for(int i = 1; i <= int(n);++(i))
#define rforn(i,n) for(int (i)=n-1;(i)>=(int)(0);--(i))
#define forlu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rforlu(i,l,u) for(int (i)=(int)(u-1);(i)>=(int)(l);--(i))
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define out(x) cout<<x<<'\n';
#define outp(x,pr) cout<<fixed<<setprecision(pr)<<x<<'\n';
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef unsigned long ul; typedef long long ll; typedef unsigned long long ull;
typedef unsigned int ui; typedef long double ld;
typedef vector<int> vi; typedef vector<bool> vb; typedef pair<int, int> pii; typedef vector<pair<int, int>> vpii;
typedef vector<double> vd; typedef pair<double, double> pdd; typedef vector<pdd> vpdd;
typedef vector<string> vs; typedef vector<ll> vll; typedef vector<ld> vld;
typedef set<int> si; typedef map<int, int> mii; typedef multimap<int, int> mmii;

#ifdef LOCAL
struct dbger {
	template<typename T> dbger& operator,(const T& v) { cerr << v << " "; return *this; }
} dbg;
#define debug(...) { cerr << #__VA_ARGS__ << " : "; dbg, __VA_ARGS__; cerr << '\n'; }
#define file "b"
//#define REOPEN freopen("test.in", "r", stdin); freopen("test.out", "w", stdout); freopen("test.err", "w", stderr);
#define REOPEN() freopen(file".in", "r", stdin); freopen(file".out", "w", stdout); freopen("test.err", "w", stderr);
struct file_stdio { file_stdio() { REOPEN() }; } file_stdio;
struct timer {
	clock_t t = clock();
	~timer() { std::cerr << "tot elapsed: " << 1000.0 * (clock() - t) / CLOCKS_PER_SEC << " ms\n"; };
} dt;
#define TSTAMP() std::cerr << "elapsed: " << 1000.0 * (clock() - dt.t) / CLOCKS_PER_SEC << " ms\n";
#else
#define debug(...)
#define REOPEN
#define TSTAMP
#endif

int main()
{
	int nt; cin >> nt;
	int t = 1;
	while (t <= nt)
	{
		string s; cin >> s;
		vector<int> v;
		for (auto ch : s) {
			v.push_back(ch - '0');
		}

		while (1)
		{		
			int m = v[0];
			int in = v.size();
			for (int i = 1; i < v.size(); ++i)
			{
				if (v[i] < m) 
				{
					in = i; break;
				}
				m = max(v[i], m);
			}

			if (in == v.size()) break;

			for (int j = in; j < v.size(); ++j) v[j] = 9;
			while (v[--in] == 0) v[in] = 9;
			v[in]--;
		}

		cout << "Case #" << t << ": ";
		int i = 0;
		while (v[i] == 0) ++i;
		while (i < v.size()) cout << v[i++];
		cout << '\n';
		++t;
	}

	return 0;
}

/****************************** END COPY *************************************/
