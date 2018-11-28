#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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

int solve(vector<bool> bits, int N)
{
	int moves = 0;
	queue<int> flips;

	REP(i, bits.sz)
	{
		if(!flips.empty() && flips.front() <= i - N)
			flips.pop();

		if((bits[i] ^ (flips.size() % 2 == 0)) == 1)
		{
			if(i > bits.size() - N)
				return -1;

			moves++;
			flips.push(i);
		} 
	}

	return moves;
}

int main()
{
	int T;cin >> T;
	REP(c,T)
	{
		string s; cin >> s;
		int N; cin >> N;

		vector <bool> bits(s.sz, false), rbits(s.sz, false);

		REP(i, s.sz)
		bits[i] = (s[i] == '+');

		rbits = bits;
		reverse(all(rbits));

		int x1 =  solve(bits, N);
		int x2 =  solve(rbits, N);

		//cout << "x1 = " <<  x1 << " x2 = " << x2 << "\n";

		int ans = (x1 != -1 && x2 != -1) ? min(x1,x2) : max(x1,x2);

		if(x1 == -1 && x2 == -1) 
		cout << "Case #" << c+1 << ": " << "IMPOSSIBLE" << "\n";
		else
		cout << "Case #" << c+1 << ": " << ans << "\n";
	}

	return 0;
}
