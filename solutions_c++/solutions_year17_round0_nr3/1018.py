#include <bits/stdc++.h>

#define sz(a) int((a).size())
#define tr(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(),(c).end()
#define uniq(c) sort(all((c))); (c).resize(unique(all((c))) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all((c)), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all((c)), (x)) - (c).begin())
#define R(i,a,b) for (int i=a; i<=b; i++)
#define Re(i,a,b) for (int i=a; i>=b; i--)
#define stop getchar();
#define tess puts("===========");
#define tes(a) cerr<< #a << " = "<< a <<endl;
#define cincout ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);

#define pb  push_back
#define mp  make_pair
#define endl "\n"

#define fi  first
#define se  second
#define x   first
#define y   second
#define between(a,b,c) ((a) >= (b) and (a) <= (c))
using namespace std;
typedef long long int64;


int main(int argc, char const *argv[])
{
	cincout;
	int T;
	cin >> T;
	R(tc,1,T) {
		map<int64,int64> frq, nxt;
		int64 n,k; cin >> n >> k;

		nxt[n] = 1;
		frq[n] = 1;

		while (!nxt.empty()) {
			auto pt = --nxt.end();
			int64 now = pt->first - 1;
			int64 cnt = pt->second;
			nxt.erase(pt);
			int64 a = now/2;
			int64 b = now - now/2;

			if (a > 0) frq[a] += cnt, nxt[a] += cnt;
			if (b > 0) frq[b] += cnt, nxt[b] += cnt;
		}

		int64 ans = -1;
		for (auto hue = frq.rbegin(); hue != frq.rend(); hue++) {
			// cout << hue->first << " " << hue->second << " " << k << endl;
			if (k <= hue->second) {ans = hue->first; break;}
			else k -= hue->second;
		}

		ans--;
		int64 a = ans/2;
		int64 b = ans - ans/2;

		cout << "Case #" << tc << ": ";
		cout << b << " " << a << endl;
	}
	return 0;
}