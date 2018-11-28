#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define len length()
#define mkp make_pair
#define pi acos(-1)
typedef long long LL;
typedef vector <int> VI;
typedef pair<int, int> PI;

int main()
{
	int T;cin >> T;
	REP(c,T)
	{
		LL D, N; cin >> D >> N;

		double maxT = 0;
		VI x(N, 0), s(N,0);
		REP(i, N)
		{
			LL xi, speedi; cin >> xi >> speedi;
			x[i] = xi; s[i] = speedi;

			xi = D - xi;

			double t = xi*1.0/speedi;
			maxT = max(maxT, t);
		}

		//cout << "maxT = " << maxT << "\n";
		//if(maxT == 0.0)
		//{
		//	cout << D << " " << N << "\n";
		//	REP(i, N) cout << x[i] << " " << s[i] << "\n";
		//}
		if(maxT > 0)
		{
			double ans = D/maxT;

			cout << "Case #" << c+1 << ": ";
			printf("%.6f\n", ans);
		}
		else
		{
			cout << "Case #" << c+1 << ": ";
			printf("0.000000\n");
		}

	}

	return 0;
}
