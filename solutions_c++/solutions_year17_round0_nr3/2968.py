#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef set<int> SI;
typedef pair<int, int> PII;
typedef vector<pair<int, int> > VPII;

const int INF = 1000000001;
const int EPS = 1e-9;
const int MOD = 1000000007;

//813437586

#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define VAR(v, n) auto v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)

#define MP make_pair
#define PB push_back
#define ST first
#define ND second


/*************************** END OF TEMPLATE ***************************/

int main()
{
	ios_base::sync_with_stdio(false);

	int W;
	cin >> W;
	for(int testcase = 1; testcase <= W; testcase++)
	{
		LL n, k;
		cin >> n >> k;

		map<LL, LL> m;
		m.clear();

		m.insert(MP(n, 1));
		LL in = 0;

		while(1)
		{
			//cout << "A " << endl;
			auto i = m.end();
			i--;
			LL l, a;
			l = i -> first;
			a = i -> second;
			m.erase(i);
			in += a;
			if(in >= k)
			{
				if((l-1)%2 == 1)
					cout << "Case #" << testcase << ": " << (l-1)/2+1 << ' ' << (l-1)/2 << '\n';
				else
					cout << "Case #" << testcase << ": " << (l-1)/2 << ' ' << (l-1)/2 << '\n';
				break;
			}
			if((l-1) % 2 == 1)
			{
				LL amm;
				if(m.find((l-1)/2) != m.end())
				{
					amm = a + m.find((l-1)/2)->second;
					m.erase(m.find((l-1)/2));
				}
				else
					amm = a;
				m.insert(MP((l-1)/2, amm));
				if(m.find((l-1)/2+1) != m.end())
				{
					amm = a + m.find((l-1)/2+1)->second;
					m.erase(m.find((l-1)/2+1));
				}
				else
					amm = a;
				m.insert(MP((l-1)/2+1 , amm));
			}
			else
			{
				LL amm;
				if(m.find((l-1)/2) != m.end())
				{
					amm = a * 2 + m.find((l-1)/2)->second;
					m.erase(m.find((l-1)/2));
				}
				else
					amm = a * 2;
				m.insert(MP((l-1)/2, amm));
			}
		}
	}
}