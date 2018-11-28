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
	int w;
	cin >> w;
	for(int ca = 1; ca <= w; ca++)
	{
	string s;
	cin >> s;
	for(int i = SIZE(s) - 2; i >= 0; i--)
	{
		if(s[i+1] < s[i])
		{
			for(int j = i+1; j < SIZE(s); j++)
				s[j] = '9';
			s[i]--;
			while(s[i] < '0')
			{
				s[i] = '9';
				i--;
				s[i]--;
			}
		}
	}
	int i;
	for(i = 0; i < SIZE(s); i++)
	{
		if(s[i] != '0')
			break;
	}
	cout << "Case #" << ca << ": ";
	for(; i < SIZE(s); i++)
	{
		cout << s[i];
	}
	cout << endl;
	}
}