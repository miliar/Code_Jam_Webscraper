/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()
#define uniq(v) (v).erase(unique(all(v)), v.end())
#define IOS ios::sync_with_stdio(0);
#define sz(v) (v).size()
#define fr(a, b, c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a, b) fr(a,0,b)
#define cl(a, b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d %d", &a, &b)
#define sc3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define pr(a) printf("%d\n", a);
#define pr2(a, b) printf("%d %d\n", a, b)
#define pr3(a, b, c) printf("%d %d %d\n", a, b, c)
#define IOS ios::sync_with_stdio(0);

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<ll, ll> pll;

int main()
{
	ifstream in; in.open("in.txt"); 
	ofstream out; out.open("out.txt");
	int t;
	in >> t;
	fr(T, 0, t)
	{
		string s;
		int k;
		in >> s >> k;
		int countFlips = 0;
		bool pos = true;
		rp(i, sz(s))
		{
			if(s[i] == '-')
			{
				if(sz(s) - i < k)
				{
					pos = false;
					break;
				}
				countFlips++;
				fr(j, i, i+k)
				{
					if(s[j] == '+')s[j] = '-';
					else if(s[j] == '-') s[j] = '+';
				}
			}
		}
		if(pos)
			out << "Case #" << T+1 << ": " << countFlips << endl;
		else
			out << "Case #" << T+1 << ": " << "IMPOSSIBLE" << endl;
	}
	out.close();
	in.close();
	return 0;
}
