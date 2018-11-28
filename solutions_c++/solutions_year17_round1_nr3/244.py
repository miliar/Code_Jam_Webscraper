/*
PROG: gcj5304486c
LANG: C++
 */
#include <cstdlib>
#include <csignal>
#include <csetjmp>
#include <cstdarg>
#include <typeinfo>
#include <bitset>
#include <functional>
#include <utility>
#include <ctime>
#include <cstddef>
#include <new>
#include <memory>
#include <climits>
#include <cfloat>
#include <limits>
#include <exception>
#include <cassert>
#include <cerrno>
#include <cctype>
#include <cwctype>
#include <cstring>
#include <cwchar>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <complex>
#include <valarray>
#include <numeric>
#include <iosfwd>
#include <ios>	
#include <istream>	
#include <ostream>
#include <iostream>
#include <fstream>	
#include <strstream>	
#include <iomanip>	
#include <streambuf>
#include <cstdio>
#include <locale>	
#include <clocale>

#define MP make_pair
#define PB push_back

#define SINF 10001
#define INF 1000000001
#define LLINF 1000000000000000001ll
#define EPS 0.000000000000001
#define PI ((4.0) * atan(1.0))
#define MAXN 101

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, long long> pil;
typedef pair<long long, int> pli;
typedef pair<long long, long long> pll;
typedef pair<pii, pii> ppp;

int T;
int H1, A1, H2, A2, B, D;
map<ppp, int> m;
priority_queue<pair<int, ppp>, vector<pair<int, ppp> >, greater<pair<int, ppp> > > pq;
int ans;

int32_t main()
{
	ios_base::sync_with_stdio(false);
	if (fopen("gcj5304486c.in", "r"))
	{	
		freopen ("gcj5304486c.in", "r", stdin);
		freopen ("gcj5304486c.out", "w", stdout);
	}
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> H1 >> A1 >> H2 >> A2 >> B >> D;
		ans = INF;
		m.clear();
		while(!pq.empty())
		{
			pq.pop();
		}
		m[MP(MP(H1, A1), MP(H2, A2))] = 1;
		pq.push(MP(1, MP(MP(H1, A1), MP(H2, A2))));
		while(!pq.empty())
		{
			auto cur = pq.top();
			pq.pop();
			//attack
			int tim = cur.first;
			int h1 = cur.second.first.first;
			int a1 = cur.second.first.second;
			int h2 = cur.second.second.first;
			int a2 = cur.second.second.second;
//			cerr << tim << ' ' << h1 << ' ' << a1 << ' ' << h2 << ' ' << a2 << endl;
			ppp attack = MP(MP(h1 - a2, a1), MP(h2 - a1, a2));
			if (attack.second.first <= 0)
			{
				ans = tim;
				break;
			}
			if (m[attack] == 0 && attack.first.first > 0)
			{
				m[attack] = tim + 1;
				pq.push(MP(tim + 1, attack));
			}
			if (a1 <= H2)
			{
				ppp buff = (MP(MP(h1 - a2, a1 + B), MP(h2, a2)));
				if (m[buff] == 0 && buff.first.first > 0)
				{
					m[buff] = tim + 1;
					pq.push(MP(tim + 1, buff));
				}
			}
			ppp cure = (MP(MP(H1 - a2, a1), MP(h2, a2)));
			if (m[cure] == 0 && cure.first.first > 0)
			{
				m[cure] = tim + 1;
				pq.push(MP(tim + 1, cure));
			}
			ppp debuff = (MP(MP(h1 - max(a2 - D, 0), a1), MP(h2, max(a2 - D, 0))));
			if (m[debuff] == 0 && debuff.first.first > 0)
			{
				m[debuff] = tim + 1;
				pq.push(MP(tim + 1, debuff));
			}
		}
		if (ans == INF)
		{
			cout << "IMPOSSIBLE\n";
		}
		else
		{
			cout << ans << '\n';
		}
		//youhealth theyhealth you attack they attack
	}
}
