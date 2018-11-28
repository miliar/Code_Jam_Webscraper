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

// Find the longest increasing prefix

int lip(string s)
{
	bool good = true;
	REP(i, s.sz-1)
	{
		if(good && s[i+1] < s[i])
		return i;
		
		good = good && true;
	}
	return s.sz-1;
}

int main()
{
	int T;cin >> T;
	REP(c,T)
	{
		string s; cin >> s;
		if(s.sz == 1)
		{
			cout << "Case #" << c+1 << ": " << s << "\n";
			continue;
		}

		int x = lip(s);

		if(x == s.sz-1)
		{
			cout << "Case #" << c+1 << ": " << s << "\n";
			continue;
		}
		
		//cout << x << " " << s.substr(0,x+1) << "\n";

		string ans = "";
		if(x == 0 || s[x] == '1')
		{
			if(s[x] != '1')
			ans += (s[x] -'0' -1 + '0');

			REP(i, x)
			ans += '9';
		}
		else
		{
			string t = s.substr(0,x+1);
			sort(all(t));
			reverse(all(t));

			char mx = t[0];
			int cnt = count(all(s), mx);

			if(cnt == 1)
			{
				REP(i, x)
				ans += s[i];
				ans += (mx -'0' - 1 + '0');
			}
			else
			{
				bool first = true;
				REP(i, x+1)
				{
					if(s[i] != mx)
					ans += s[i];
					else
					{
						if(first)
						{
							first = false;
							ans += (mx -'0' - 1 + '0');
						}
						else
						{
							ans += '9';
						}
					}
				}
			}
		}

		FOR(i, x+1, s.sz)
		{
			ans += '9';
		}
		cout << "Case #" << c+1 << ": " << ans << "\n";
		
	}

	return 0;
}
