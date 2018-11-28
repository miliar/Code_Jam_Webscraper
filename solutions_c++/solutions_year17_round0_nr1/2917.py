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

const int maxn = 200;
bool happy[maxn];



int main()
{
	ios_base::sync_with_stdio(false);
	int W;
	cin >> W;
	for (int w = 1; w <= W; w++)
	{
		string s;
		int k;
		cin >> s >> k;
		for(int i = 0; i < SIZE(s); i++)
			happy[i] = (s[i] == '+');
		int n = SIZE(s);
		int ans = 0;
		for(int i = 0; i <= n-k; i++)
			if(!happy[i])
			{
				ans++;
				for(int j = i; j < i+k; j++)
					happy[j] = !happy[j];
			}

		bool can = true;
		for(int i = 0; i < n; i++)
			if(!happy[i])
				can = false;
		if(can)
			cout << "Case #" << w << ": " << ans << '\n';
		else
			cout << "Case #" << w << ": " << "IMPOSSIBLE" << '\n';
	}

}